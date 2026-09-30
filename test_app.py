from app import app


def test_get_product_success():
    client = app.test_client()
    resp = client.get("/products/p_1")
    assert resp.status_code == 200
    assert resp.get_json()["name"] == "Widget"


def test_get_product_not_found():
    client = app.test_client()
    resp = client.get("/products/p_99")
    assert resp.status_code == 404


def test_get_product_bad_format():
    client = app.test_client()
    resp = client.get("/products/xyz")
    assert resp.status_code == 400


def test_list_products():
    client = app.test_client()
    resp = client.get("/products")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 3


def test_price_with_discount():
    client = app.test_client()
    resp = client.get("/products/p_2/price")  # p_2 is "electronics", has a 10% discount
    print(resp.status_code, resp.get_json())
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["price_cents"] == 1200
    assert data["discounted_price_cents"] == 1080  # 1200 * (1 - 0.10)


def test_price_no_discount():
    client = app.test_client()
    resp = client.get(
        "/products/p_1/price"
    )  # p_1 is "hardware", no discount configured
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["discounted_price_cents"] == data["price_cents"]  # unchanged, 0% off


if __name__ == "__main__":
    test_get_product_success()
    test_get_product_not_found()
    test_get_product_bad_format()
    test_price_with_discount()  # <- add
    test_price_no_discount()
    print("all existing tests passed")
