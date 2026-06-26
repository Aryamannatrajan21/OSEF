# Rule Writing Guide

How to author a Rule for the OSEF Engineering Policy Engine.

## 1. Implementation
Extend `osef.epe.core.rule.Rule` and implement `evaluate(context: RuleContext)`.

## 2. Evidence & Recommendations
A rule must **never** return a primitive score. It must return a `Finding` object containing structured `Evidence` (why the rule fired) and a `Recommendation` (how the engineer can fix it).

## 3. AutoFix
If a rule violation can be automatically resolved via source code mutation, the rule should populate the `AutoFix` metadata on the `Finding`.
