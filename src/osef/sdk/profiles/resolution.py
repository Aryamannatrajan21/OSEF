"""
Profile Resolution Engine.
"""

from typing import Dict, Set, List, Optional
from osef.sdk.profiles.profile import EngineeringProfile
from osef.sdk.profiles.registry import get_default_profiles
from osef.contracts.exceptions import OSEFError


class ProfileResolutionEngine:
    """
    Resolves composed and inherited profiles into a final unified configuration.
    """

    def __init__(self, registry: Optional[Dict[str, EngineeringProfile]] = None, disable: Optional[List[str]] = None):
        self.registry = registry or get_default_profiles()
        self.disable_plugins = set(disable or [])

    def resolve(self, profile_name: str) -> EngineeringProfile:
        """
        Resolves a profile by name, including its inheritance chain, 
        and applies any plugin exclusions.
        """
        if profile_name not in self.registry:
            raise ValueError(f"Unknown profile: {profile_name}")

        resolved = self._resolve_recursive(self.registry[profile_name], {profile_name})
        
        # Apply exclusions
        if self.disable_plugins:
            resolved.plugins = [p for p in resolved.plugins if p not in self.disable_plugins]
            resolved.capabilities = [c for c in resolved.capabilities if c not in self.disable_plugins]
            
        return resolved

    def _resolve_recursive(
        self, profile: EngineeringProfile, seen: Set[str]
    ) -> EngineeringProfile:
        plugins = set(profile.plugins)
        policy_packs = set(profile.policy_packs)
        projections = set(profile.projections)
        dashboards = set(profile.dashboards)
        capabilities = set(profile.capabilities)
        certification_levels = set(profile.certification_levels)

        for parent_name in profile.inherits:
            if parent_name in seen:
                raise OSEFError(
                    f"Circular inheritance detected in profile: {parent_name}"
                )
            seen.add(parent_name)

            if parent_name not in self.registry:
                raise OSEFError(f"Parent profile '{parent_name}' is not registered.")

            parent_resolved = self._resolve_recursive(
                self.registry[parent_name], seen
            )

            plugins.update(parent_resolved.plugins)
            policy_packs.update(parent_resolved.policy_packs)
            projections.update(parent_resolved.projections)
            dashboards.update(parent_resolved.dashboards)
            capabilities.update(parent_resolved.capabilities)
            certification_levels.update(parent_resolved.certification_levels)

        return EngineeringProfile(
            name=profile.name,
            description=profile.description,
            inherits=profile.inherits,  # Keep original inherits for tracing
            plugins=list(plugins),
            policy_packs=list(policy_packs),
            projections=list(projections),
            dashboards=list(dashboards),
            certification_levels=list(certification_levels),
            capabilities=list(capabilities),
        )
