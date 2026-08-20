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


if __name__ == "__main__":
    test_get_product_success()
    test_get_product_not_found()
    test_get_product_bad_format()
    print("all existing tests passed")
