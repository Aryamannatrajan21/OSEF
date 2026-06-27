import time
from osef.core.ekg import KnowledgeGraph
from osef_architecture.plugin import ArchitectureEnricher
import argparse

def benchmark_architecture(target_dir: str):
    print(f"Benchmarking architecture intelligence parsing for: {target_dir}")
    
    graph = KnowledgeGraph()
    enricher = ArchitectureEnricher()
    
    start_time = time.time()
    delta = enricher.enrich(None, graph)
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    print("\n--- Architecture Benchmark Results ---")
    print(f"Execution Time: {execution_time:.4f} seconds")
    print("\n--- Graph Quality ---")
    print(f"Architectural Nodes Discovered: {len(delta.nodes_to_add)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default=".", help="Directory to parse")
    args = parser.parse_args()
    benchmark_architecture(args.dir)
