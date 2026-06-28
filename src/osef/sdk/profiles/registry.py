"""
Default Profiles Registry.
"""

from typing import Dict
from osef.sdk.profiles.profile import EngineeringProfile, CertificationLevel


def get_default_profiles() -> Dict[str, EngineeringProfile]:
    return {
        "core": EngineeringProfile(
            name="core",
            description="Base OSEF parsing and EKG",
            plugins=["osef-core"],
            certification_levels=[CertificationLevel.BASIC],
        ),
        "backend": EngineeringProfile(
            name="backend",
            description="Backend engineering profile",
            inherits=["core"],
            plugins=["osef-architecture", "osef-security", "osef-infrastructure"],
            certification_levels=[CertificationLevel.STANDARD],
        ),
        "frontend": EngineeringProfile(
            name="frontend",
            description="Frontend engineering profile",
            inherits=["core"],
            plugins=["osef-architecture"],
            certification_levels=[CertificationLevel.BASIC],
        ),
        "cloud": EngineeringProfile(
            name="cloud",
            description="Cloud engineering profile",
            inherits=["backend"],
            plugins=["osef-runtime"],
            certification_levels=[CertificationLevel.STRICT],
        ),
        "security": EngineeringProfile(
            name="security",
            description="Security-focused profile",
            inherits=["core"],
            plugins=["osef-security"],
            certification_levels=[CertificationLevel.STRICT],
        ),
        "enterprise": EngineeringProfile(
            name="enterprise",
            description="Enterprise organizational profile",
            inherits=["backend", "security", "runtime"],
            plugins=["osef-enterprise"],
            certification_levels=[CertificationLevel.ENTERPRISE],
        ),
        "runtime": EngineeringProfile(
            name="runtime",
            description="Runtime telemetry profile",
            inherits=["core"],
            plugins=["osef-runtime"],
        ),
        "compliance": EngineeringProfile(
            name="compliance",
            description="Compliance profile",
            inherits=["enterprise"],
            certification_levels=[CertificationLevel.ENTERPRISE],
        ),
        "ai": EngineeringProfile(
            name="ai",
            description="AI Engineering Intelligence profile",
            inherits=["enterprise"],
        ),
    }
