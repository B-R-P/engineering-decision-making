# Decision-method router

Use this reference for any Level 3 decision, or a Level 2 decision that is unfamiliar, mixes problem types, or lacks an obvious primary method. Start with the central question, then read the specialist file it points to. The mapping is a starting point.

| Central question | Primary method | Add when relevant | Specialist reference |
|---|---|---|---|
| What does the user need, and what is in scope? | Requirements and constraint analysis | Assumption testing, focused clarification, first-principles reframing (strip inherited assumptions) | [Problem-solving methods](problem-solving.md) |
| What should I inspect, try, or delegate next? | Information gain and value of information | Tool cost, task dependencies, authority checks | [Problem-solving methods](problem-solving.md) for investigation; [Verification and delivery](verification-and-delivery.md) for tool/delegation choices |
| Why does this behavior or failure occur? | Hypothesis-driven diagnosis | Causal reasoning, controlled reproduction, fault isolation | [Problem-solving methods](problem-solving.md) |
| What behavior must remain correct? | Invariants, contracts, state-transition reasoning | Counterexamples, property-based checks | [Problem-solving methods](problem-solving.md) |
| Which dependency, data design, or architecture fits best? | Consequence-based trade-off comparison | Pareto analysis, MCDA, ATAM-style scenarios, lifecycle and reversibility analysis | [Design and architecture](design-and-architecture.md) |
| Is a performance change worthwhile? | Profiling and representative measurement | Complexity analysis, workload modeling, benchmark comparison | [Design and architecture](design-and-architecture.md) |
| What should be tested, reviewed, or accepted? | Risk-based verification against requirements and contracts | Boundary analysis, regression testing, property/contract tests, independent review | [Verification and delivery](verification-and-delivery.md) |
| What could be abused or compromised? | Threat modeling and trust-boundary analysis | Abuse cases, security invariants, privacy analysis | [Verification and delivery](verification-and-delivery.md) |
| What could fail in production? | Failure-mode and effects analysis (FMEA), state/fault analysis | Fault injection, observability and recovery checks | [Verification and delivery](verification-and-delivery.md) |
| How can data or interfaces change safely? | Contract and compatibility analysis | Expand-and-contract migration, versioning, rollback planning | [Verification and delivery](verification-and-delivery.md) |
| What is worth doing first, or not doing at all? | Value, urgency, and dependency analysis | Cost of delay, expected value, critical-path reasoning | [Verification and delivery](verification-and-delivery.md) |
| How should a change be released or recovered? | Blast-radius and rollout analysis | Canary/staged deployment, rollback triggers, incident signals | [Verification and delivery](verification-and-delivery.md) |
| Should we invest in flexibility or refactoring? | Lifecycle-cost and change-frequency analysis | Reversibility, sensitivity, real-options reasoning | [Design and architecture](design-and-architecture.md) |
| Is the leading option merely the incumbent, a convention, or the first adequate one? | Divergence and local-minima moves | Constraint ablation, tail sampling, altitude shift, inversion, dual-track | [Divergence and local minima](divergence-and-local-minima.md) |

## Routing rules

1. Select the primary method based on what is uncertain or must be established, not on framework familiarity.
2. Combine methods only when they answer different material questions. A schema migration may need contract analysis, failure analysis, and rollout planning.
3. Apply hard constraints and authorization checks before preference ranking. Benefit comparisons cannot override a gate (SKILL §1).
4. Prefer methods that produce decision-relevant evidence: measurement for performance, discriminating tests for diagnosis, and concrete scenarios for architectural quality conflicts.
5. Use specialist detail only when the short mapping is insufficient. Avoid loading unrelated references.
6. If no listed method fits, use a suitable method from general engineering or domain knowledge. The table is not a whitelist.
