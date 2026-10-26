---
name: engineering-decision-making
description: "Use when a coding agent must make a non-trivial judgment about requirements, investigation, debugging, implementation, architecture, testing, risk, prioritization, tools, or delivery. Choose a reasoning method suited to the problem and scale effort to impact, uncertainty, scope, and reversibility."
---

# Engineering Decision-Making

Make the best-supported decision for the actual problem with the least analysis sufficient for its risk. Be quick on local choices, thoughtful on intermediate trade-offs, and rigorous when consequences are high. Decision quality matters more than following a process or naming a framework.

Use general engineering knowledge, repository evidence, available tools, authoritative documentation, and any suitable reasoning method. The methods and references are starting points, not a whitelist. Adapt, combine, or replace them when the problem calls for it.

## 1. Calibrate effort and authority

Assess **impact**, **uncertainty**, **scope**, and **reversibility**. Code size alone does not indicate risk.

- **Level 1 — Local:** low-impact and easy to reverse. Follow user preferences and repository conventions; choose the simplest adequate option and proceed. Keep analysis implicit. Do not run the full workflow unless a meaningful trade-off or risk appears.
- **Level 2 — Substantive:** alternatives or uncertainty have meaningful consequences within a limited scope. Inspect relevant context, compare a small set of credible options, and investigate assumptions that could change the decision.
- **Level 3 — Consequential:** cross-cutting, high-risk, operationally sensitive, or hard to reverse. Examine affected boundaries, failure modes, lifecycle consequences, recovery, and decision-critical uncertainty. Validate important assumptions and record the rationale when future work will need it.

Set the level **provisionally**: the first look at a constraint often reads broader or narrower than it is, and the cheapest discriminating check (§5) corrects it — let the level follow the check.

Establish what the user authorized: recommendation, investigation, implementation, or an action with external effects. Treat explicit requirements, policy, authorization, security, privacy, and data-integrity obligations as gates—not preferences that other benefits can offset. Close an open question with evidence before asking it: hunt the fact that settles it. Ask when the choice is the user's own and no evidence can settle it, naming the evidence that would have closed it. Otherwise proceed with a safe, stated assumption.

**Complete when:** the effort level, requested scope, and decision authority are clear, and relevant hard constraints have been identified.

## 2. Frame the actual problem

For Level 2 and 3 decisions, inspect the smallest useful slice of context: repository instructions, relevant code and call sites, tests, types and contracts, dependency versions, configuration, logs, or deployment paths as the question requires. Do not inspect everything by default.

Define the desired outcome and observable success conditions. Separate facts, inferences, assumptions, and unknowns when the distinction could change the choice. Challenge the proposed solution when a different problem framing could better satisfy the underlying need. Include doing nothing, reducing scope, or running a small experiment when credible.

**Complete when:** the objective, scope, material constraints, and decision question are clear enough for the calibrated effort level.

## 3. Explore before converging

Choose exploration to fit the problem:

- For diagnosis, form competing explanations and seek evidence that distinguishes them.
- For design, consider materially different approaches, including the simplest adequate option and the current approach; include a non-obvious alternative when it could offer a meaningful advantage.
- For requirements or plans, test the framing and consider a different goal, sequence, or smaller experiment.
- For action selection, compare the value of inspecting, testing, measuring, asking, escalating, implementing, deferring, or making no change.

Treat conventions as evidence, not unquestionable rules. Consider unconventional, hybrid, or assumption-changing solutions when useful, then evaluate them against the same constraints and evidence as familiar approaches. Explore more broadly when novelty or the cost of a missed option is high. For ordinary choices, a small credible set is enough; do not invent alternatives to fill a quota.

**Complete when:** the key hypotheses, options, or next actions are represented and further exploration is unlikely to reveal a materially different contender at reasonable cost.

## 4. Select the method that fits

Choose a reasoning method based on the central uncertainty or property to establish—not on which framework is familiar. Combine methods when they answer different material questions. Use the method references below when they add concrete guidance; use the router when the problem is mixed, unfamiliar, or the method choice is unclear.

- **When the decision type or method is unclear:** read the [decision-method router](references/decision-method-router.md), especially for mixed or unfamiliar Level 2 and 3 decisions.
- **For requirements, investigation, diagnosis, correctness, or algorithm/data-structure decisions:** read [problem-solving methods](references/problem-solving.md).
- **For implementation, dependency, data-design, architecture, performance, lifecycle-cost, or flexibility choices:** read [design and architecture methods](references/design-and-architecture.md).
- **For testing, review, security, reliability, prioritization, tool/delegation, compatibility, migration, release, or recovery decisions:** read [verification and delivery methods](references/verification-and-delivery.md).

Load only the detail needed for the current branch.

**Complete when:** the selected method fits the actual decision and can produce evidence or comparisons that support it.

## 5. Evaluate evidence and resolve consequential uncertainty

Compare options against the same relevant requirements. Separate hard constraints from preferences and remove infeasible options before ranking. Consider downstream consequences—correctness, users, dependencies, compatibility, operations, maintenance, lifecycle cost, failure modes, and future change—when they matter.

Prefer repository evidence, executable checks, representative measurements, and authoritative version-matched documentation over unsupported assumptions. Label estimates as estimates. Account for costs shifted to other components, teams, operators, or future maintainers.

For substantive or consequential decisions, challenge the leading conclusion:

- What evidence would change it?
- Under what plausible condition would another option be better?
- Could a simpler, safer, or fundamentally different approach solve the real problem?
- What happens if the most consequential assumption is wrong?

Investigate the unknown most likely to change the decision or reveal unacceptable risk. Choose the cheapest credible discriminating check. For an experiment, identify the question, representative conditions, and result that would change the decision. Use scores or probabilities only when their inputs are defensible and the calculation adds value.

**Complete when:** decision-changing unknowns are resolved, bounded by explicit assumptions, or mitigated; remaining risks are acceptable for the calibrated level.

## 6. Decide, act, and verify

Choose the feasible option that best fits the user's goal and evidence. When approaches are similarly effective, prefer a good fit with the existing system, less unnecessary complexity, acceptable lifecycle cost, and a clear path to change. Familiarity and speculative future scale alone are not decisive.

Stop when the leading choice is supported well enough for the risk, no unresolved and reasonably testable unknown is likely to change it enough to justify its cost, and the remaining risks are accepted, stated, or mitigated. If no option is adequately supported, take the next best step: investigate, ask a focused question, escalate it — naming the decision, its owner, and your recommendation — propose a reversible experiment, or explain what remains unresolved.

Act within the request: recommend when asked to recommend; implement when asked to implement. For implementation, make the smallest coherent change that solves the actual problem. Run relevant tests, type checks, lint/build checks, benchmarks, or security/compatibility checks in proportion to impact. Report checks that were not run and material residual uncertainty. Record a decision where future work will look for it: an ADR when it is hard to reverse, surprising without context, and the result of a real trade-off; a comment at the site otherwise.

**Complete when:** the requested decision or change is complete, relevant verification has been performed or its limits are stated, and important risks or reconsideration triggers are communicated accurately.

## Response shape

Keep the response proportional to the decision:

- **Level 1:** usually proceed without a formal explanation; mention rationale only if useful.
- **Level 2:** state the recommendation, decisive trade-off, strongest alternative, and important assumption or check.
- **Level 3:** summarize the objective and constraints, credible options, decisive evidence and trade-offs, residual risks, validation/recovery, and reconsideration triggers as relevant.

Use a table, score, diagram, or decision record only when it improves the result. Do not mistake lengthy analysis for decision quality or manufacture certainty when the evidence does not support a single winner.
