from flask import Flask
from routes import catalog_bp

app = Flask(__name__)
app.register_blueprint(catalog_bp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
