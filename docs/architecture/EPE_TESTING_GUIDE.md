# EPE Testing Guide

Every rule in the EPE must be thoroughly tested in isolation.

## 1. Mocks
Since Rules only consume `RuleContext`, you can easily mock a graph of 5 nodes to trigger a rule violation, completely bypassing the file parser.

## 2. Explainability Verifications
Rule tests must assert that `Finding.evidence` and `Finding.recommendation` are populated correctly. An unexplainable finding is considered a failed test.
