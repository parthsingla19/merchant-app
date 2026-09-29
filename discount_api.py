"""
Mock discount API. DO NOT EDIT.
Run in its own terminal:  python discount_api.py
Listens on http://localhost:6100

GET /discount?category=<category>
  -> {"category": ..., "discount_pct": int}
  -> 404 if that category has no discount configured
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

DISCOUNTS = {
    "electronics": 10,
    # "hardware" deliberately not here -> triggers the "no discount, default 0" path
}


@app.route("/discount")
def discount():
    category = request.args.get("category")
    if category not in DISCOUNTS:
        return jsonify({"error": "no discount for category"}), 404
    return jsonify({"category": category, "discount_pct": DISCOUNTS[category]})


if __name__ == "__main__":
    app.run(port=6100, debug=True)
