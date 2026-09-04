# AI Worklog System Instructions

## Project Role

You are helping with the project that contains this `.ai/` folder.

Treat the project files and the `.ai/` worklog files as the source of truth. Do not rely only on chat history or tool memory.

## Startup Routine

Before doing project work:

1. Read `.ai/AI_WORKLOG.md` if it exists.
2. Read `.ai/AGENTS.md`.
3. Read `.ai/PROJECT_CONTEXT.md` if it exists and the task needs broader context.
4. Inspect only the files needed for the current task.
5. Summarize the current state, assumptions, and next action before making non-trivial changes.

If `.ai/START_HERE.md` exists, read it as the startup checklist.

## Working Style

- Be direct and practical.
- Prefer small, reversible changes.
- Use existing project patterns before adding new structure.
- Ask before destructive, broad, or irreversible changes.
- Do not delete or overwrite important files without explicit permission.
- Keep written output concise and useful for the next human or AI session.
- When changing code or documents, list the files touched and why.

## AI Worklog Requirement

Maintain `.ai/AI_WORKLOG.md` as the project handoff log.

Update `.ai/AI_WORKLOG.md` automatically after meaningful progress, including:

- files changed
- decisions made
- bugs fixed
- features added
- blockers discovered
- project state clarified
- next action changed
- verification results changed the known state

Do not update the worklog for trivial actions like reading files, answering a small question, or making no project change.

When updating the worklog:

1. Update the current state if status, priority, warning, or next action changed.
2. Append a concise session entry under `Session Log`.
3. Include context read, files touched, commands/checks run, result, and next step.
4. Do not paste full transcripts.
5. Do not duplicate Git history; summarize the outcome.

## Definition Of Done

Before saying a task is done:

- Confirm what changed.
- Mention files touched.
- Mention checks or verification performed.
- Mention any remaining risk or missing test.
- Update `AI_WORKLOG.md` if meaningful progress happened.

