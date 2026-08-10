"""In-memory product catalog. No database needed."""

PRODUCTS = {
    "p_1": {"name": "Widget", "price_cents": 500, "category": "hardware"},
    "p_2": {"name": "Gadget", "price_cents": 1200, "category": "electronics"},
    "p_3": {"name": "Gizmo", "price_cents": 800, "category": "electronics"},
}


def get_product(product_id):
    return PRODUCTS.get(product_id)


def all_products():
    return PRODUCTS
