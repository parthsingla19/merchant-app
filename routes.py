from flask import Blueprint, jsonify
from services.catalog import get_product, all_products
import requests

catalog_bp = Blueprint("catalog", __name__)


@catalog_bp.route("/products/<product_id>")
def get_product_route(product_id):
    if not product_id.startswith("p_"):
        return jsonify({"error": "invalid product id format"}), 400
    product = get_product(product_id)
    if product is None:
        return jsonify({"error": "product not found"}), 404
    return jsonify({"id": product_id, **product})


@catalog_bp.route("/products", methods={"GET"})
def get_all_products():
    products = all_products()
    return [{"id": pid, **info} for pid, info in products.items()]


@catalog_bp.route("/products/<id>/price")
def get_discount(id):
    product = get_product(id)
    if product is None:
        return {"error": "product not found"}, 404

    try:
        resp = requests.get(
            "http://localhost:6100/discount",
            params={"category": product["category"]},
            timeout=5,
        )
    except requests.RequestException:
        return {"error": "discount service unreachable"}, 502

    if resp.status_code == 200:
        discount_pct = resp.json()["discount_pct"]
    elif resp.status_code == 404:
        discount_pct = 0
    else:
        return {"error": "discount service failed"}, 502

    discounted_price_cents = round(product["price_cents"] * (1 - discount_pct / 100))
    return {
        "id": id,
        "name": product["name"],
        "price_cents": product["price_cents"],
        "discounted_price_cents": discounted_price_cents,
    }
