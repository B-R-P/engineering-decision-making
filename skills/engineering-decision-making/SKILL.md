---
name: engineering-decision-making
version: 5.1.2
description: "Use when a coding agent must make a non-trivial judgment about requirements, investigation, debugging, implementation, architecture, performance, testing, risk, prioritization, tool use, delivery, migration, or compatibility. Calibrates analysis depth and search breadth to impact, uncertainty, scope, and reversibility, and escapes local minima before committing."
---

# Engineering Decision-Making

Make the best-supported decision with the least analysis the risk justifies and the widest search the stakes demand. Be quick on local choices, deliberate on trade-offs, rigorous when consequences are high. Decision quality beats process or framework names.

Use general engineering knowledge, repository evidence, tools, authoritative docs, and any suitable reasoning method. Treat methods and references as starting points; add one from general engineering when the problem calls for it.

## 1. Calibrate depth and breadth

Assess **impact**, **uncertainty**, **scope**, and **reversibility**. Code size does not indicate risk. Two dials move independently:

**Depth — how hard to think about the leading option:**

- **Level 1 — Local:** low impact, easy to reverse. Follow conventions and user preference; take the simplest adequate option; keep analysis implicit. Run the full workflow only when a real trade-off appears.
- **Level 2 — Substantive:** alternatives or uncertainty carry meaningful consequence within a limited scope. Inspect context, compare a small credible set, test assumptions that could flip the choice.
- **Level 3 — Consequential:** cross-cutting, high-risk, operationally sensitive, or hard to reverse. Examine boundaries, failure modes, lifecycle, recovery, and decision-critical unknowns; validate load-bearing assumptions; record the rationale.

**Breadth — how wide to search before choosing:**

- **Narrow:** the problem matches a known pattern and the leading option is already evidence-backed. Take it.
- **Broad:** the problem is unfamiliar, or the leading option is the incumbent, a convention, or the first adequate one. Compare a small set of *solution families*.
- **Forced-diverse:** a missed better option is plausible and expensive. Sample the tail and check the leader against at least one different family.

Set both **provisionally**: the first look often reads broader or narrower than it is; let the cheapest discriminating check (§5) correct the rating.

**Search stop — a cost decision, not a level.** Stop searching when a materially better option is unlikely or the cost of searching exceeds its expected gain. It is wrong when a better option is plausible and being wrong is expensive. Widen the search before deepening it.

**Authority and gates.** Establish what the user authorized: recommendation, investigation, implementation, or an action with external effects. Treat explicit requirements, legal/regulatory obligations, policy, authorization and user scope, security, privacy, and data-integrity as **gates**, not preferences other benefits offset. A choice is genuinely the user's when it is a gate decision or no evidence can settle it; otherwise proceed on a safe, stated assumption. Ask only for those, naming the evidence that would have closed the question.

**Complete when:** depth, breadth, requested scope, and decision authority are clear, and hard constraints are identified.

## 2. Frame the actual problem

For Level 2/3, inspect the smallest useful slice: instructions, code and call sites, tests, types and contracts, dependency versions, config, logs, or deployment paths as the question requires.

Define the outcome and **observable** success conditions. Separate facts, inferences, assumptions, and unknowns where the distinction changes the choice. Ask whether a different problem framing — a different goal, smaller scope, or doing nothing — better serves the underlying need.

**Treat a proposal as a hypothesis.** When the user names a solution, identify the bottleneck it assumes and verify that bottleneck with the cheapest evidence before adopting it. Evidence-first beats agreement; the most common agent failure is a confident, well-formatted answer to the wrong premise.

**Take the outside view.** Ask how decisions like this usually fail, and whether this plan looks like the base rate. The inside view optimizes the plan; the outside view catches the trap it is walking into.

**Complete when:** the objective, scope, constraints, and decision question are stated; every hard constraint is named; facts, assumptions, and unknowns are separated where the distinction changes the choice.

## 3. Diverge, then converge

**Generate without judging, then evaluate.** Premature evaluation is the main cause of local minima: the first adequate answer wins because it was judged while still forming.

Choose exploration to fit the problem:

- **Diagnosis:** competing explanations; seek evidence that distinguishes them.
- **Design:** candidate *solution families*, not variants of one idea; sample the tail when breadth is forced.
- **Requirements/plans:** test the framing; consider a different goal, sequence, or smaller experiment.
- **Action:** compare inspecting, testing, measuring, asking, escalating, implementing, deferring, and no change.

Conventions are evidence, not rules. Evaluate unconventional and hybrid options against the same constraints as familiar ones.

At **Narrow** breadth, one adequate option wins; generate candidates only when doing so could change the decision. At **Broad** or **Forced-diverse** breadth — or when the leading option is the incumbent, a convention, or the first adequate one — load [divergence and local minima](references/divergence-and-local-minima.md) for the concrete moves.

**Complete when:** the credible families for this breadth are represented, the tail is sampled when breadth is forced, and further search is unlikely to surface a materially different contender.

## 4. Select the method that fits

Choose by the central uncertainty to resolve, then by fit. Combine methods only when they answer different questions.

- **Unfamiliar, mixed, or lacking an obvious primary method, or any Level 3 decision:** [decision-method router](references/decision-method-router.md) — a method index, not an exhaustive taxonomy.
- **Requirements, investigation, unclear behaviour, diagnosis, correctness, algorithms:** [problem-solving](references/problem-solving.md).
- **Dependency, data design, architecture, performance, lifecycle:** [design and architecture](references/design-and-architecture.md).
- **Testing, security, reliability, prioritization, tools, compatibility, migration, release, recovery:** [verification and delivery](references/verification-and-delivery.md).

Each reference is short; read the whole file for the branch you selected.

**Complete when:** the method fits the decision and can produce evidence or comparisons that support it.

## 5. Test the leader before you trust it

Compare options against the same requirements. Remove options that violate hard constraints before ranking. Weigh downstream costs — correctness, users, dependencies, compatibility, operations, maintenance, lifecycle, failure modes, future change.

**Tier the evidence:** executable checks and representative measurement first; then direct repository evidence about this codebase; then current, version-matched docs; then analogy or convention. Use the best tier available, and say which one you used. Label estimates as estimates. When tiers disagree, name the conflict and prefer the evidence most relevant to the claim: measurement for performance, this repository for behavior, docs for external contracts.

**Level 2 — slim adversarial pass (skip when the leader is already evidence-backed at Narrow breadth):** steelman the runner-up if one exists, run one external check (test, measurement, retrieval), and record the observation that would reverse the decision.

**Level 3 — full adversarial pass:**

- **Structured pre-mortem:** enumerate at least three failures, mostly *boring* ones (timeline slip, an untracked consumer breaks, the rollback path fails), then their consequences and mitigations, before committing.
- **Steelman the runner-up:** argue the second-best option wins. If the leader survives, you have earned the conclusion.
- **Externally check the falsifier:** state what would reverse the decision, then check it now with a test, measurement, retrieval, or human review. If no check is possible, record the gap as the reconsideration trigger and lower your confidence.
- **Score the genuine unknowns** where *probability wrong × impact ÷ cost to check* is highest.
- **Attack the most confident assumption,** not the easiest one.

**Calibrate, don't assert.** Estimate confidence from convergence across independent signals — repeated samples, tool/test results, retrieval coverage — not from how confident the wording feels. State a range or tier, not a bare probability.

**Evidence complete when:** decision-changing unknowns are resolved, bounded by explicit assumptions, or mitigated.

## 6. Decide, act, verify, learn

Choose the feasible option that best fits the goal and evidence. When options are similarly effective, decide on fit with the existing system, less unnecessary complexity, acceptable lifecycle cost, and a clear path to change.

**Acceptance stop.** Proceed when the evidence meets the §5 bar, no reasonably testable unknown would change the choice enough to justify the cost, and remaining risks are accepted, stated, or mitigated. If nothing is adequately supported, take the next step: investigate, ask a focused question, escalate with a recommendation, propose a reversible experiment, or state what remains unresolved.

Act within the request: recommend when asked to recommend, implement when asked to implement. For implementation, make the smallest coherent change. Run tests, type checks, lint/build, benchmarks, or security/compatibility checks in proportion to impact; report what you did not run and the residual uncertainty.

**Record and revisit.** For a decision that is hard to reverse, surprising without context, or the product of a real trade-off, write a short record using the [decision-record template](references/verification-and-delivery.md#decision-records). Persist it where future work looks; set a **reconsideration trigger** and note dismissed risks with the reason.

**Gap check.** For Level 3 or a recorded decision, name one category this analysis likely under-explored — regulatory, reputational, second-order, motivational — and flag it as an open question.

**Complete when:** the decision or change is complete, verification is done or its limits stated, and important risks and reconsideration triggers are communicated.

## Response shape

Proportional to the decision:

- **Level 1:** proceed; mention rationale only if useful.
- **Level 2:** recommendation, decisive trade-off, strongest alternative, key assumption or check.
- **Level 3:** objective and constraints, credible options across families, decisive evidence and trade-offs, residual risks, the falsifier or reconsideration trigger, validation/recovery.

Use a table, score, or decision record only when it improves the result. Keep analysis proportional; length is not quality, and certainty belongs only where the evidence supports it.

## Failure modes

- Over-analyzing a local choice; under-searching a consequential one.
- Accepting the user's proposed solution without testing the bottleneck.
- Treating a convention or price as a hard constraint.
- Evaluating while generating, so the first adequate idea wins.
- Three options that are one idea reworded.
- Trusting intrinsic self-critique without an external check.
- A green test suite read as proof of untested properties.
- Claiming a check that was never run.
- Recording a commitment but not a dismissed risk.
