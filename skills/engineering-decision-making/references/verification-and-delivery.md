# Verification, risk, prioritization, and delivery methods

Load this reference when deciding what to test, whether a change is acceptable, how to handle security or reliability, how to evolve contracts/data or migrate, how to choose tools or delegate, what work to prioritize, or how to release and recover safely.

## Test selection and acceptance

Select verification according to the behavior and failure modes that matter, not merely the convenience of existing tests.

- Test the changed contract and the regression that motivated the change.
- Use boundary and equivalence analysis for inputs; contract or property-based tests when general properties matter; integration and end-to-end tests for cross-boundary behavior.
- Use risk-based testing to prioritize failures by likelihood, consequence, and detectability. Critical paths may warrant stronger evidence than low-impact code.
- For review and acceptance, compare the change with acceptance criteria, callers and consumers, invariants, security and compatibility constraints, and actual test evidence.
- Report the checks performed and the gaps that remain. A green test suite is evidence, not proof that untested properties are correct.

## Security and privacy

Use threat modeling when a change affects identity, authorization, sensitive data, external input, trust boundaries, secrets, or privileged actions.

1. Identify assets, trust boundaries, entry points, actors, and security/privacy properties.
2. Consider plausible misuse and failure paths, including cross-tenant access, privilege escalation, injection, replay, data exposure, and unsafe defaults as applicable.
3. Identify mitigations that satisfy hard requirements and fit the actual threat model.
4. Verify important mitigations with focused tests, static/dynamic checks, or expert review where warranted.

Security, privacy, legal, and policy constraints are feasibility gates (SKILL §1). A general score or convenience benefit cannot compensate for violating them. The skill supports technical reasoning but does not replace required organizational or expert review.

## Reliability, concurrency, and failure analysis

Use state-machine or fault analysis when retries, concurrency, partial failure, timeouts, queues, shared state, or external dependencies matter. Consider failure modes by cause, effect, likelihood, detectability, and recovery cost. This is failure-mode and effects analysis (FMEA) in lightweight form: enumerate the modes, score severity, likelihood, and detectability, and prioritize by the resulting risk rather than by intuition. Pay particular attention to duplicate side effects, ordering, deadlocks, resource exhaustion, cascading failure, and loss of observability where relevant. For state-changing operations, verify idempotency with duplicate and partial requests, not just the happy path.

Use fault injection or simulation only when it meaningfully tests the risk. Define expected behavior under failure, the signal that reveals failure, and recovery behavior.

## APIs, compatibility, and data migrations

Before changing a public or shared interface, identify consumers and their supported versions. Build a compatibility matrix when multiple versions or clients coexist. Preserve contracts or plan a versioned transition.

For schema/data migrations, analyze old and new application compatibility, backfills, constraints, partial completion, locking/downtime, data correctness, and rollback limits. Prefer staged or expand-and-contract changes when they materially reduce deployment risk. Recognize that some data transformations cannot be rolled back without a restore or compensating migration; make recovery explicit.

## Prioritization and sequencing

To decide what is worth doing, compare user/business value, urgency or cost of delay, risk reduction, dependencies, and effort. Impact-effort matrices are a rough aid; use cost-of-delay or expected-value reasoning only when inputs are meaningful. Distinguish task priority (what matters) from sequencing (what must happen first). When tasks depend on one another, identify the critical path — the longest chain of dependent work — and protect it; parallel work off the critical path does not shorten delivery. Favor early work that removes a major dependency or tests a costly assumption, and deliver coherent increments that can be checked independently.

## Tool use and delegation

Choose a tool call or delegated task when expected information, quality, or parallel speed justifies its cost. Define the question the tool should resolve, the expected output, and what action would follow from the result. Use read-only inspection before risky actions when it can resolve uncertainty. Parallelize independent work; keep work with tight dependencies coordinated. Check authority, privacy, scope, and side effects before using tools or delegating actions. Follow environment instructions and tool constraints.

## Deployment, rollout, and recovery

For consequential releases, consider blast radius, backward compatibility, observability, rollout stages, user impact, rollback feasibility, and data changes. Establish relevant health signals and explicit rollback or pause triggers. Canary, feature flags, shadow traffic, or gradual rollout are useful only when they provide meaningful risk reduction and the system can safely support them. State how to recover from partial failure and which changes are not safely reversible.

## Decision records

Record a consequential decision when its context will matter to future work or the choice is cross-cutting or costly to reverse. Follow repository conventions. A concise record can include:

- Context, goal, and hard constraints.
- Decision and scope.
- Credible alternatives and decisive trade-offs.
- Evidence, assumptions, residual risks, and dismissed risks with the reason.
- Verification, rollout/recovery plan, and triggers for reconsideration.

For a trivial or easily reversible choice, preserve the rationale in the code or response only if useful.
