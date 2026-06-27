from osef.core.ekg import KnowledgeGraph, GraphDelta
from osef.sdk.registry.correlation_registry import CorrelationRegistry
from osef.sdk.pipeline import PipelineContext
import logging

logger = logging.getLogger(__name__)


class CorrelationEngine:
    """
    Executes all rules in the CorrelationRegistry against the EKG,
    producing cross-domain GraphDeltas.
    """

    def __init__(self, registry: CorrelationRegistry):
        self.registry = registry

    def execute(self, context: PipelineContext, graph: KnowledgeGraph) -> GraphDelta:
        logger.info("Starting Cross-Domain Correlation...")
        merged_delta = GraphDelta()

        for rule in self.registry.get_rules():
            logger.info(f"Evaluating correlation rule: {rule.name}")
            try:
                rule_delta = rule.evaluate(graph)

                # Merge the deltas
                if rule_delta:
                    merged_delta.nodes_to_add.extend(rule_delta.nodes_to_add)
                    merged_delta.edges_to_add.extend(rule_delta.edges_to_add)

            except Exception as e:
                logger.error(f"Error evaluating rule {rule.name}: {e}")

        return merged_delta
