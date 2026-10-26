# Engineering Decision-Making

This repository contains the **Engineering Decision-Making** skill for coding
agents. It helps an agent choose an appropriate level of analysis for a task,
investigate the real problem before accepting a proposed solution, compare
credible alternatives when needed, and verify that the chosen action works.

## Why it is helpful

Engineering tasks fail not only because of incorrect code, but also because
the wrong problem was solved, an important constraint was missed, or a
reasonable-looking first option was accepted too quickly. This skill makes
decision quality proportional to the task:

- small, reversible choices stay quick;
- uncertain or consequential choices receive broader investigation;
- security, compatibility, privacy, and data-integrity constraints are treated
  as gates;
- decisions are checked with evidence, tests, measurements, or explicit
  assumptions;
- important trade-offs and conditions for revisiting a decision are recorded.

The result is less over-analysis for routine work and fewer costly mistakes
for changes that are difficult to reverse.

## Installation

```bash
npx skills add B-R-P/building-deterministic-tools
```

## Contents

- [`skills/engineering-decision-making/SKILL.md`](skills/engineering-decision-making/SKILL.md)
  — the skill instructions.
- [`skills/engineering-decision-making/references/`](skills/engineering-decision-making/references/)
  — focused guidance for problem solving, architecture, divergence, method
  selection, and verification.
- [`skills/engineering-decision-making/evals/`](skills/engineering-decision-making/evals/)
  — behavioral evaluation cases and fixtures.
