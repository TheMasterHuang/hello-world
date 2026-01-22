---
name: draft-commit-message
description: Draft a Conventional Commits message when the user asks for help writing a commit message.
---
Draft a Conventional Commits message in the form: type(scope): summary

Rules:
- Use imperative mood (Add/Fix/Refactor/Update).
- Keep summary <= 72 characters.
- If breaking change, add footer: BREAKING CHANGE: <desc>

Ask for missing info if needed:
- type? scope? key change summary?
