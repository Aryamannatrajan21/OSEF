"""
Adapters for extracting organizational context.
"""

from pathlib import Path
import yaml
from osef.core.ekg import GraphDelta, Node, Edge


class CodeownersAdapter:
    """Parses .github/CODEOWNERS files to infer ownership edges."""

    def parse(self, workspace_dir: Path) -> GraphDelta:
        delta = GraphDelta()
        codeowners_path = workspace_dir / ".github" / "CODEOWNERS"

        if not codeowners_path.exists():
            # Try root CODEOWNERS
            codeowners_path = workspace_dir / "CODEOWNERS"
            if not codeowners_path.exists():
                return delta

        with open(codeowners_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                parts = line.split()
                if len(parts) >= 2:
                    path_pattern = parts[0]
                    owners = parts[1:]

                    # Add edges connecting path pattern to owners
                    for owner in owners:
                        # Clean up @ from @team names
                        owner_id = owner.lstrip("@")
                        delta.edges_to_add.append(
                            Edge(
                                source_id=path_pattern,  # Simplified: in reality we map pattern to actual files
                                target_id=f"team:{owner_id}",
                                relation_type="OWNED_BY",
                            )
                        )

        return delta


class OrgChartAdapter:
    """Parses an organizational chart (e.g., teams.yaml)."""

    def parse(self, workspace_dir: Path) -> GraphDelta:
        delta = GraphDelta()
        teams_path = workspace_dir / "teams.yaml"

        if not teams_path.exists():
            return delta

        with open(teams_path, "r") as f:
            data = yaml.safe_load(f) or {}
            teams = data.get("teams", {})

            for team_name, team_info in teams.items():
                team_id = f"team:{team_name}"
                delta.nodes_to_add.append(
                    Node(id=team_id, type="Organizational.Team", name=team_name)
                )

                members = team_info.get("members", [])
                for member in members:
                    member_id = f"member:{member}"
                    delta.nodes_to_add.append(
                        Node(id=member_id, type="Organizational.Member", name=member)
                    )

                    delta.edges_to_add.append(
                        Edge(
                            source_id=team_id,
                            target_id=member_id,
                            relation_type="HAS_MEMBER",
                        )
                    )

        return delta
