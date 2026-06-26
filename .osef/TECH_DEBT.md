# Active Technical Debt

- Python `ast` parser cannot preserve formatting or exact tokens (makes code-generation difficult without `libcst`).
- EPE runs completely in memory. Huge repositories (>5M LOC) will cause OOM.
- No Windows path resolution testing currently in CI.
