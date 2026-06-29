# Benchmark Case Studies

Case Studies go beyond raw metrics to demonstrate OSEF's Engineering Intelligence capabilities on real-world projects. They provide concrete examples of the questions OSEF can answer.

## Case Study Template Structure

Every case study generated in the `benchmarks/case-studies/` directory must adhere to the following structure:

### 1. Project Overview
A brief description of the project, its ecosystem, and why it was selected for the Benchmark Corpus.

### 2. Repository Statistics
Raw size metrics (lines of code, number of files, primary languages).

### 3. Architecture Overview
A high-level summary of the extracted C4 architecture.

### 4. Engineering Questions Answered
The core of the case study. Examples of complex engineering questions that OSEF successfully answered for this repository.
* *Example (Kubernetes):* Which deployments expose services?
* *Example (Spring Boot):* What are the cyclic dependencies between services?

### 5. Graph Screenshots / Visualizations
Embedded visual representations of the graph (`graph.png`, `architecture.png`).

### 6. Performance & Certification
A summary of the runner metrics (Time, Memory, Engineering Confidence).

### 7. Findings & Lessons Learned
Any interesting architectural anomalies, policy violations, or structural insights discovered by OSEF during the benchmark run.

## Video Demonstrations
Video demonstrations of the CLI or UI answering the "Engineering Questions" should be linked in the corresponding Case Study document to provide persuasive evidence of OSEF's capabilities.
