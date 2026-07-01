"""
Enterprise Dashboards.
"""


def get_dashboards() -> dict:
    return {
        "ownership_dashboard": {
            "title": "Ownership Dashboard",
            "panels": ["Orphaned Services", "Team Load"],
        },
        "compliance_dashboard": {
            "title": "Compliance Dashboard",
            "panels": ["SOC2 Status", "Missing Controls"],
        },
        "governance_dashboard": {
            "title": "Governance Dashboard",
            "panels": ["Unapproved Architectures", "Stale Owners"],
        },
        "service_catalog": {
            "title": "Service Catalog",
            "panels": ["All Services", "Product Mapping"],
        },
    }
