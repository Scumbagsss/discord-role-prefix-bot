# Architecture

## Purpose

Synchronizes Discord nicknames with role-based clan and faction prefixes.

## Boundary

The public repository documents only the system boundary. The production edition contains private implementation details, persistence schemas, operational thresholds, adapters, credentials and deployment configuration.

## Components

- **Discord interaction layer** — buttons, forms, commands and/or event listeners.
- **Domain service layer** — validates state and executes the project-specific workflow.
- **Persistence/integration layer** — private production storage and external adapters.
- **Observability layer** — staff logs, error handling and operational feedback.

## Workflow

1. Observe role/nickname state
2. Resolve active managed prefix
3. Normalize base nickname
4. Apply synchronized nickname
5. Persist manager changes

## Why the implementation is private

The production code is a commercial/private implementation. The portfolio edition intentionally prevents direct deployment while still documenting the engineering scope.
