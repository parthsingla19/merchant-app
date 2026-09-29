# Product Catalog Service

## Existing (already here — read before touching anything)
- `app.py`    — entrypoint
- `routes.py` — GET /products/<id>
- `services/catalog.py` — the data + get_product/all_products
- `test_app.py` — 3 existing passing tests

Run: `pip install flask requests` then `python app.py` (port 5000).
Run tests: `python test_app.py`

## Part 1 — Add a list endpoint
`GET /products` — return all products as a list (reuse `all_products()` from
`services/catalog.py`, don't re-read the data yourself). Add a test.
Commit.

## Part 2 — Add a discount-lookup feature
A discount service exists at `http://localhost:6100/discount?category=<cat>`
(mock, I'll give you the file separately, don't build it). It returns
`{"category", "discount_pct"}` or 404 if that category has no discount.

Add `GET /products/<id>/price` returning:
```
{"id", "name", "price_cents", "discounted_price_cents"}
```
If the discount service has no discount for the product's category, treat
`discount_pct` as 0 (price unchanged) — this is a "missing means default"
case, not an error. If the discount service is unreachable, 502.
Add a test for both the discounted and no-discount paths. Commit.

## Part 3 — Extend, don't duplicate
Add `GET /products?category=<cat>` (filter the list from Part 1 by category,
query param optional — no param means all products, same as Part 1).
Reuse Part 1's logic, don't copy it. Add a test. Commit.

## Git checklist (the actual point of this repo)
- Read the existing code and run the existing tests BEFORE your first edit.
- One commit per part, with a real message.
- `git log --oneline` should show your 3 new commits sitting on top of the
  3 that were already here when you cloned it.
- Push after each commit.
