# CLAUDE.md

## Project

Python Telegram/WhatsApp bot. FastAPI backend, MongoDB, async.

## Architecture

- DDD: modular by domain in src/, each module: router.py, schemas.py, models.py, service.py, dependencies.py,
  exceptions.py
- Constants: src/const.py, import as `from src import const`, use as `const.PROVIDER_GROQ`
- Stdlib imports: `import datetime`, `import typing` — import the module, not names from it.
  Use `datetime.datetime`, `datetime.timezone.utc`, `typing.Optional`, etc.
  Never use `from datetime import UTC` — use `datetime.UTC` instead.
- Settings: split BaseSettings per module
- Max 500 lines per file — decompose if exceeded
- FastAPI conventions: see .claude/skills/fastapi.md

## Commands

- Lint: `uv run ruff check --fix`
- Format: `uv run ruff format`
- Test: `uv run pytest`
- Coverage must be >= 85%

## Code style

Enforced by ruff. See pyproject.toml `[tool.ruff]` for full config.
Do not duplicate ruff rules here — if ruff can check it, ruff owns it.

## Testing

- Trophy testing: fast integration tests, real DB (mongomock), minimal mocks
- Mocks only at external boundaries: HTTP API, Telegram Bot API, WhatsApp API
- Fixtures in tests/fixtures.py as @pytest.fixture, accessed via test parameters (NOT via import)
- pytest_plugins already configured in conftest.py
- asyncio_mode = "auto" in pyproject.toml — pytestmark not needed

## Git

- Conventional commits (feat:, fix:, docs:, refactoring:)
- Always PR, never push to main
- Max ~500 lines of diff per commit — split large tasks into logical commits
- When accumulated uncommitted changes approach ~500 lines, stop and propose a commit before continuing

## Security review

Before finishing any task, check for:

- Secrets/tokens leaking into logs, responses, or error messages
- Injection: NoSQL, command injection, template injection
- Input validation: all user input validated via Pydantic before use
- Authorization: no endpoints accessible without proper auth checks
- Rate limiting: new public endpoints must have rate limits
- Dependencies: no known vulnerabilities in added packages

## Documentation

After code changes, update documentation:

- README.md — if functionality, commands, or setup changed
- User-facing help — if commands/features changed (all localization languages)
- Do not create separate doc files without necessity — keep README.md up to date

## Before finishing

1. `uv run ruff check --fix`
2. `uv run ruff format`
3. `uv run pytest`
4. Verify coverage >= 85%
5. Security review (see above)
6. Update documentation (see "Documentation" section above)

Do not finish until lint, tests, and security review pass.

## Gotchas

- Comments and logs in English
- Frontend: Solid.js
