Title: Add Feature — Product Store

When to use
-----------
Use this prompt to request a new feature or API change for the Product Store Flask app.

Required information
--------------------
- Feature name: Short descriptive name.
- Motivation: Why the feature is needed and what problem it solves.
- API surface: List endpoints to add/change (HTTP method, path).
- Frontend changes: What to change in `index.html` (form fields, buttons, table columns).
- Data model: In-memory shape (e.g., product: {id:int, name:str, price:float}).
- Validation rules: required fields, ranges, types.
- Acceptance criteria: Concrete checks that prove the feature works (manual or automated).
- Tests to add: Which unit/integration tests to create or update.

Constraints / project rules
--------------------------
- Keep to the project's constraints: single HTML frontend and in-memory storage. Do not add a database.
- Keep changes minimal and isolated. Include tests for behavior changes.

Example prompt
--------------
Feature name: Update product price
Motivation: Allow merchants to change a product's price without recreating the product.
API surface:
- PUT /products/<id> — payload: {"price": 9.99}
Frontend changes: Add an "Edit" button per row; show a modal or inline form to edit price.
Data model: product: {id: int, name: str, price: float}
Validation rules: price must be a positive float; 2 decimal precision.
Acceptance criteria:
- PUT returns 200 and updated product JSON
- UI updates to show new price without full page reload
Tests to add:
- API test for PUT /products/<id> success and invalid price case
- End-to-end test demonstrating UI edit flow (Playwright)

Run instructions (for maintainers)
-------------------------------
Start the server and run the new tests with `pytest`. Use Playwright when e2e tests are requested.
# Add Feature

You are working on a Flask product store API with a plain HTML frontend.

Before writing any code:
1. Check AGENTS.md for project context
2. Check existing code to understand current structure
3. Tell me what you plan to change before changing it

Then implement the feature cleanly with no unnecessary additions.