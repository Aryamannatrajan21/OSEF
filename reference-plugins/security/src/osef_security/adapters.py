from osef.core.ekg import GraphDelta
from .skm import SKM


class BaseSecurityAdapter:
    def parse(self, filepath: str) -> GraphDelta:
        raise NotImplementedError


class TrivyAdapter(BaseSecurityAdapter):
    def parse(self, filepath: str) -> GraphDelta:
        # Mocking trivial vulnerability translation
        delta = GraphDelta()
        vuln = SKM.create_node(
            type_name=SKM.VULNERABILITY.value,
            name="CVE-2026-9999",
            source_adapter="TrivyAdapter",
            metadata={"severity": "CRITICAL"},
        )
        delta.nodes_to_add.append(vuln)
        return delta


class BanditAdapter(BaseSecurityAdapter):
    def parse(self, filepath: str) -> GraphDelta:
        # Mocking static analysis translation
        delta = GraphDelta()
        finding = SKM.create_node(
            type_name=SKM.FINDING.value,
            name="B101:assert_used",
            source_adapter="BanditAdapter",
            metadata={"severity": "LOW"},
        )
        delta.nodes_to_add.append(finding)
        return delta
