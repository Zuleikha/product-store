Title: Write Tests — Product Store

Purpose
-------
Use this prompt to ask an agent to write tests (unit, integration, or end-to-end) for the Product Store project.

Provide the following details
-----------------------------
- Scope: `unit` / `integration` / `e2e`.
- Target files / endpoints: which functions, routes, or UI flows to test.
- Examples of expected behavior: success case(s) and failure case(s).
- Test framework: `pytest` for backend; Playwright for browser e2e.
- Any fixtures or test data to include.

Testing conventions
-------------------
- Place backend tests alongside existing `test_validation.py` style, using `pytest`.
- Keep tests deterministic and fast. Use monkeypatching for time/network if needed.
- For e2e tests, prefer Playwright and run against a running dev server at `http://127.0.0.1:5000`.

Example prompt
--------------
Scope: integration
Target endpoints: POST /products, GET /products
Expected behavior:
- POST /products with valid payload returns 201 and created product JSON
- POST /products with missing name returns 400 and error message
Fixtures: start server with empty in-memory store; seed a sample product for GET tests.

Desired outputs
---------------
- One or more `pytest` test files added/updated.
- Clear instructions for running tests locally:

```bash
python -m venv .venv
pip install -r requirements.txt
pytest -q
```

If e2e tests are requested, include Playwright install/run steps and a sample `playwright` test.
# Write Tests

Write pytest unit tests for the Flask product store API.

Cover:
- Happy path for each endpoint
- Missing fields
- Invalid data types
- Non-existent product IDs

Use the existing app.py. Do not modify it.