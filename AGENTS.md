# AGENTS.md

# MemoriaOS Hermes Adapter

## Purpose

This repository contains the Hermes Agent implementation of MemoriaOS.

Its responsibility is to execute the specifications defined in the
`memoria-spec` repository using Hermes Agent.

This repository is an implementation layer.

It is **not** the source of truth for system behaviour.

---

# Source of Truth

The authoritative project repositories are:

| Repository | Responsibility |
|------------|----------------|
| memoria-spec | Architecture, specifications, ADRs, schemas |
| memoriaos-hermes | Hermes implementation |
| memoria-repository | Persistent knowledge repository |

When implementation conflicts with a specification:

**The specification always wins.**

Never silently change behaviour defined by a specification.

---

# Repository Responsibilities

This repository may contain:

- Hermes Jobs
- Hermes Skills
- Hermes Prompts
- Hermes Scripts
- Hermes Templates
- Hermes Configuration
- Tests

This repository must NOT contain:

- architecture decisions
- business specifications
- duplicated documentation from memoria-spec
- repository data

---

# Development Principles

When implementing new functionality:

1. Read the corresponding specification first.
2. Implement the minimum working solution.
3. Prefer incremental improvements.
4. Keep implementations deterministic whenever practical.
5. Make repository writes traceable.
6. Avoid hidden side effects.
7. Fail explicitly rather than silently ignoring errors.

---

# Working with Specifications

Before implementing any feature:

1. Locate the corresponding specification in `memoria-spec`.
2. Treat the specification as authoritative.
3. If implementation reveals a problem in the specification:

   Do NOT silently work around it.

   Instead:

  - document the issue;
  - propose a specification update;
  - keep implementation behaviour explicit.

---

# Working with memoria-repository

The repository is the persistent storage of MemoriaOS.

Rules:

- Never modify repository files manually from prompts.
- Always use approved Jobs or Scripts.
- Preserve reproducibility.
- Preserve traceability.
- Never destroy information without an explicit specification.

---

# Hermes Guidelines

Use Hermes features whenever they simplify the implementation.

Prefer:

- Skills for reusable expertise
- Scripts for deterministic execution
- Cron Jobs for scheduling
- AGENTS.md for repository-wide instructions

Avoid placing large procedural logic inside Skills.

Keep Skills focused and reusable.

---

# Repository Layout

```
config/
jobs/
processes/
prompts/
scripts/
skills/
templates/
tests/
```

---

# Code Style

Prefer:

- readable code;
- small modules;
- explicit naming;
- predictable behaviour.

Avoid:

- unnecessary abstractions;
- premature optimisation;
- duplicated logic.

---

# Testing

Every new Script should be executable independently.

Whenever possible:

- produce deterministic output;
- make failures reproducible;
- keep dependencies explicit.

---

# Git

Keep commits small.

One logical change per commit.

Commit message format:

```
type: short description
```

Examples:

```
feat: add observation pipeline
fix: repository writer
docs: update AGENTS
refactor: simplify metadata generation
```

---

# Current Milestone

Sprint 1

Objective:

Implement OBS-PIPELINE-001.

Success criteria:

A scheduled Hermes Job receives an Observation and stores it correctly in `memoria-repository`.

---

# Target Platform

Hermes Agent v0.18.2
