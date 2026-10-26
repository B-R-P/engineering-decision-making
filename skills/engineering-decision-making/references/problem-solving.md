# Problem framing, investigation, diagnosis, and correctness

Load this reference when the main decision involves requirements, investigation, unclear behavior, root-cause analysis, algorithms and data structures, or preserving behavioral correctness.

## Problem framing and requirements

- Translate the request into an observable outcome or decision question. Identify the user-visible behavior, acceptance conditions, scope, and hard constraints.
- Separate stated requirements from inferred preferences, implementation suggestions, and assumptions. Challenge a proposed solution when a different framing could satisfy the underlying need better.
- Ask one precise question that names the missing fact when it is genuinely the user's choice — a gate such as policy, authorization, security, privacy, or data integrity — and cannot be inferred. Avoid broad escalation. Otherwise state a safe assumption and proceed.
- Include doing nothing, narrowing the scope, or running a small experiment when these are credible options.

## Investigation and information gain

Choose the next inspection or tool action by asking: what result could change my understanding or decision, how much would it help, and what will it cost in time, tool use, or risk?

- Prefer the smallest observation that distinguishes plausible explanations or resolves a decision-critical unknown.
- Inspect repository instructions, call sites, types, tests, logs, configuration, versions, and documentation according to the question—not as a universal checklist.
- Use authoritative, version-matched documentation for external behavior that is version-sensitive or changing.
- Stop exploring an area when the findings cannot affect the decision and no important risk depends on it.

For designing an experiment around a decision threshold, see [experiments and value of information](design-and-architecture.md#experiments-and-value-of-information).

## Hypothesis-driven debugging

1. Establish the observed failure and how to reproduce it; distinguish symptoms from inferred causes.
2. Generate a small set of plausible causes grounded in the evidence.
3. For each cause, identify a prediction or observation that should differ if it is true.
4. Choose the least costly reliable test that discriminates between the leading hypotheses.
5. Update or reject hypotheses based on results; repeat if the cause remains uncertain and further investigation is worthwhile.
6. Confirm the root cause with a regression test or other evidence when feasible; verify that the fix addresses the cause without creating a second failure.

When evidence is ambiguous, keep multiple hypotheses alive. Avoid repeatedly changing code without a testable explanation for why the change should work.

## Correctness, contracts, and state

Use invariants and contracts when behavior must be preserved or edge cases matter.

- Define relevant preconditions, postconditions, invariants, state transitions, ownership rules, and side effects.
- Identify boundary cases, invalid states, retries, duplicate inputs, ordering, concurrency, and partial completion where relevant.
- Check callers and consumers as well as the implementation. A locally correct function can violate a wider contract.
- Use examples, counterexamples, property-based tests, type checks, or small formal reasoning as proportionate to the risk.
- For data or state mutation, define idempotency, atomicity, consistency, and recovery where applicable; verify duplicate and partial requests with [test selection](verification-and-delivery.md#test-selection-and-acceptance).

## Algorithm and data-structure choices

Start with the required behavior and real input shape. Compare correctness, expected input sizes, time and space complexity, implementation clarity, and compatibility. Use asymptotic reasoning to eliminate obviously unsuitable approaches; for measurement of a real system, see [performance and measurement](design-and-architecture.md#performance-and-measurement). Optimize a demonstrated bottleneck rather than an imagined one.
