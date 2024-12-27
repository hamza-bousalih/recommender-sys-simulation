from flask import Flask, request, jsonify
from flask_cors import CORS
import random

from api.generate_product import generate_products, generate_products_score
from model import recommande

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.after_request
def apply_cors_policy(response):
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

@app.route('/items', methods=['GET'])
def get_items():
    user_id = request.args.get('userid', type=int)
    count = request.args.get('count', type=int)
    if count is None:
        count = 20
    
    if user_id not in users:
        products = generate_products(random.sample(range(1, 1_000), count))
        return jsonify({"products": products})
    
    items = list(range(1, 1_000))
    top_items = recommande(user_id, items, count)
    products = generate_products_score(top_items)

    return jsonify({"products": products})

if __name__ == '__main__':
    app.run(debug=True)
