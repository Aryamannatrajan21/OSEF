import json
import os
import glob

results_dir = "benchmarks/results/latest"
projects = sorted(os.listdir(results_dir))

markdown = """### 🏆 Live Benchmark Results

<details>
<summary><b>Click to expand the latest OSEF Benchmark Metrics</b></summary>
<br/>

| Project | Runtime (ms) | Memory (MB) | Nodes | Edges | Confidence Score |
| :--- | :--- | :--- | :--- | :--- | :--- |
"""

for p in projects:
    metrics_file = os.path.join(results_dir, p, "metrics.json")
    if os.path.exists(metrics_file):
        with open(metrics_file) as f:
            data = json.load(f)
            runtime = data.get("runtime_ms", "N/A")
            memory = data.get("memory_mb", "N/A")
            nodes = data.get("nodes", "N/A")
            edges = data.get("edges", "N/A")
            conf = data.get("engineering_confidence", "N/A")
            
            # Format numbers nicely
            runtime_fmt = f"{runtime:,}" if isinstance(runtime, (int, float)) else runtime
            memory_fmt = f"{memory:,}" if isinstance(memory, (int, float)) else memory
            nodes_fmt = f"{nodes:,}" if isinstance(nodes, (int, float)) else nodes
            edges_fmt = f"{edges:,}" if isinstance(edges, (int, float)) else edges
            
            markdown += f"| **{p}** | {runtime_fmt} | {memory_fmt} | {nodes_fmt} | {edges_fmt} | {conf}% |\n"

markdown += """
</details>

"""

with open("README.md", "r") as f:
    content = f.read()

target = "---\n\n## 📁 Repository Structure"
if target in content:
    new_content = content.replace(target, markdown + target)
    with open("README.md", "w") as f:
        f.write(new_content)
    print("Updated README.md successfully.")
else:
    print("Could not find the target location in README.md")

