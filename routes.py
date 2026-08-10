from flask import Blueprint, jsonify
from services.catalog import get_product

catalog_bp = Blueprint("catalog", __name__)


@catalog_bp.route("/products/<product_id>")
def get_product_route(product_id):
    product = get_product(product_id)
    if product is None:
        return jsonify({"error": "product not found"}), 404
    return jsonify({"id": product_id, **product})
