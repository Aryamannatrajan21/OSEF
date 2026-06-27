import time
from osef.core.ekg import KnowledgeGraph
from osef_infrastructure.plugin import InfrastructureEnricher
from osef.sdk.pipeline import PipelineContext
import argparse

def benchmark_graph_quality_and_performance(target_dir: str):
    print(f"Benchmarking infrastructure parsing for: {target_dir}")
    
    context = PipelineContext(workspace_dir=target_dir)
    graph = KnowledgeGraph()
    enricher = InfrastructureEnricher()
    
    start_time = time.time()
    delta = enricher(context, graph)
    end_time = time.time()
    
    # Simulate graph merge
    for node in delta.nodes_to_add:
        graph.add_node(node)
    for edge in delta.edges_to_add:
        graph.add_edge(edge)
        
    execution_time = end_time - start_time
    
    nodes = graph.get_nodes()
    edges = graph.get_edges()
    
    # Graph Quality Metrics
    resources_discovered = len(nodes)
    relationships_discovered = len(edges)
    
    provenance_accuracy = 0
    for node in nodes:
        if "source_adapter" in node.metadata and "source_file" in node.metadata:
            provenance_accuracy += 1
            
    prov_pct = (provenance_accuracy / resources_discovered * 100) if resources_discovered > 0 else 0
    
    print("\n--- Benchmark Results ---")
    print(f"Execution Time: {execution_time:.4f} seconds")
    print("\n--- Graph Quality ---")
    print(f"Resources Discovered: {resources_discovered}")
    print(f"Relationships Discovered: {relationships_discovered}")
    print(f"Provenance Accuracy: {prov_pct:.2f}% ({provenance_accuracy}/{resources_discovered})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default=".", help="Directory to parse")
    args = parser.parse_args()
    benchmark_graph_quality_and_performance(args.dir)
