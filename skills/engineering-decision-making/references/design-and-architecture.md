# Design and architecture methods

Load this reference when comparing alternatives, choosing a library or data design, or evaluating performance, architecture, lifecycle cost, and future flexibility.

## General trade-off comparison

For each credible option, compare the consequences that matter to this decision: benefit, cost, risk or failure mode, key assumptions, operational implications, and reversibility. Use the same requirements across options. Include the current approach and a no-change or staged option when credible. Keep the comparison concise unless the decision warrants more.

## Pareto dominance

Option A dominates option B when A is at least as good on every relevant dimension and better on at least one, assuming neither hides a constraint violation. Remove dominated options before weighing preferences. Multiple non-dominated options may remain; use priorities, evidence, downside risk, and reversibility to distinguish them.

## Multi-Criteria Decision Analysis (MCDA)

Use only when several viable options compete across multiple important criteria and priorities can be stated meaningfully.

1. Remove options that violate hard constraints before scoring.
2. Choose a small, non-duplicative set of criteria tied to the goal.
3. Derive weights from explicit requirements or stakeholder priorities; explain material subjective judgments.
4. Rate candidates on the same scale and record evidence for consequential ratings.
5. Treat the total as a summary of assumptions, not a substitute for judgment.
6. Test plausible changes to weights and ratings. If a small change reorders the winner, treat the result as fragile.

If uncertainty in scores exceeds the difference between options, do not claim a meaningful numerical winner.

## Architecture and quality-attribute scenarios

Use ATAM-style reasoning (Architecture Tradeoff Analysis Method) when quality attributes interact—for example performance, security, availability, modifiability, and deployability.

Describe concrete scenarios with a stimulus, operating environment, affected component, expected response, and measurable threshold where possible. Identify:

- **Sensitivity points:** small changes that cause large quality effects.
- **Trade-off points:** improving one attribute harms another.
- **Risks:** assumptions or choices that could cause failure.
- **Evidence gaps:** claims needing a prototype, measurement, or operational proof.

Use plausible workloads, incidents, requirements, or anticipated changes rather than generic quality checklists.

## Uncertainty, decision trees, and sensitivity

Use decision trees or expected utility when candidates have materially different uncertain outcomes or decisions unfold in stages. Use only defensible probabilities and consequences; represent uncertainty honestly instead of inventing numeric estimates.

Use scenario or sensitivity analysis when the winner depends on assumptions such as workload, data size, latency target, failure rate, cost, or team capability. Vary assumptions likely to matter, not every imaginable future. Prefer a robust option when it remains acceptable across plausible conditions. If a small assumption change reverses the result, gather better evidence or account for reversibility and downside protection.

## Experiments and value of information

A test or prototype is worthwhile when its result could change the decision or materially reduce risk and the value of learning exceeds the cost. The general method lives in [investigation and information gain](problem-solving.md); the design-specific rule is that the experiment must be representative of the real workload.

A useful experiment names the decision question, representative conditions, and result that would change the choice. For example: "Does this query meet the p95 latency target at representative data volume?" A prototype without a decision threshold can create activity without resolving uncertainty.

## Performance and measurement

Prove the bottleneck before changing anything: profile or measure representative workloads, then optimize the demonstrated cost. Use realistic data volume, concurrency, and I/O; report p95/p99 rather than the mean. Use complexity analysis to eliminate obviously unsuitable approaches, then measure where constants, allocation, caching, or I/O decide. State the threshold that makes the change worthwhile; a change without a decision threshold is activity, not engineering.

## Data and state design

Choose the shape from access patterns and invariants, not from habit. Decide keys and identifiers, normalization versus denormalization, indexes, ownership, lifecycle, and the consistency the task actually needs. Make invalid states hard to represent; make retries idempotent where duplicate side effects matter. Weigh migration cost and rollback limits before committing to a schema; see [APIs, compatibility, and data migrations](verification-and-delivery.md).

## Build, buy, reuse, or defer

Compare an existing capability, a maintained dependency, a focused in-house implementation, and deferral when each is credible. Check requirements fit, license and security implications, platform and version support, ecosystem maturity, maintenance effort, upgrade path, lock-in, and exit cost. Verify vendor or library claims against authoritative documentation and a representative proof of concept when a claim is decision-critical.

## Lifecycle cost and reversibility

Account for implementation, integration, tests, hosting, monitoring, support, incident response, maintenance, upgrades, migration, training, lock-in, and removal. Include costs transferred to future maintainers or other teams.

Move quickly on cheap, reversible choices. Raise the evidence and review bar for choices that are expensive to reverse. A staged rollout, interface seam, shadow read, feature flag, or pilot is worthwhile when the future flexibility it preserves exceeds the added complexity and operational burden. Treat such staging as a real option: pay the flexibility premium only when the uncertain future decision is valuable enough to justify it.
