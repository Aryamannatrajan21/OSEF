import time
from osef.core.ekg import KnowledgeGraph
from osef_security.plugin import SecurityEnricher
import argparse

def benchmark_security(target_dir: str):
    print(f"Benchmarking security intelligence parsing for: {target_dir}")
    
    graph = KnowledgeGraph()
    enricher = SecurityEnricher()
    
    start_time = time.time()
    delta = enricher.enrich(None, graph)
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    print("\n--- Security Benchmark Results ---")
    print(f"Execution Time: {execution_time:.4f} seconds")
    print("\n--- Graph Quality ---")
    print(f"Findings Discovered: {len(delta.nodes_to_add)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default=".", help="Directory to parse")
    args = parser.parse_args()
    benchmark_security(args.dir)
