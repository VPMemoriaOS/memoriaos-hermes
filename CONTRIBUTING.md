# Contributing

## Development Workflow

MemoriaOS follows a strict engineering workflow.

Every implementation starts from a specification.

```
Specification
        ↓
Implementation
        ↓
Tests
        ↓
Commit
```

Implementation must never contradict the specification.

---

## Development Rules

### Specification First

All new functionality MUST be specified in `memoria-spec`
before implementation begins.

If no specification exists, create it first.

---

### Small Commits

Development proceeds in small incremental steps.

Each commit should:

- implement one completed task;
- compile successfully;
- keep the project runnable.

Avoid large multi-purpose commits.

---

### No Unnecessary Refactoring

If existing code works correctly,
do not refactor it during unrelated work.

Only change code required for the current task.

---

### Root Cause Fixes

When a failure occurs:

1. identify the root cause;
2. fix only that cause;
3. verify the result;
4. continue development.

Avoid opportunistic changes.

---

### Deterministic Behaviour

Implementation should be deterministic whenever practical.

Avoid hidden side effects.

Preserve provenance and traceability.

---

## Testing

Every new feature must include appropriate tests.

### Test Isolation

Tests MUST NEVER use the production repository.

Always use a temporary repository created by pytest.

Example:

```python
repository_root = tmp_path / "memoria-repository"
```

Tests must not create artifacts inside the developer's working
repository.

---

### Integration Tests

Integration tests should validate complete processing pipelines
instead of isolated implementation details whenever possible.

Current end-to-end pipeline:

```
CompilationUnit
        ↓
Observation
        ↓
Evidence
        ↓
Claim
        ↓
Knowledge
        ↓
Memory
```

---

### Regression Tests

Every fixed bug should receive a regression test whenever practical.

---

## Repository Rules

Python scripts are executed with:

```bash
python3 script.py
```

Do not commit executable permission changes unless intentionally required.

---

## Commit Style

Use Conventional Commits.

Examples:

```
feat:
fix:
docs:
refactor:
test:
chore:
```

Commit messages should describe one completed piece of work.

---

## Engineering Principles

- Keep changes small.
- Keep the system runnable.
- Keep specifications authoritative.
- Keep artifacts immutable.
- Keep provenance complete.
- Keep tests isolated.
- Move forward in small verified steps.
