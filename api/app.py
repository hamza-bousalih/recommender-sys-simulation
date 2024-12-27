from flask import Flask, request, jsonify
from flask_cors import CORS
import random

from data import get_items_ids, get_rand_items, get_user, get_items
from generate_product import generate_products, generate_products_score
from model import recommande

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.after_request
def apply_cors_policy(response):
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

@app.route('/items', methods=['GET'])
def items_api():
    user_id = request.args.get('userid', type=int)
    count = request.args.get('count', type=int)
    if count is None:
        count = 20
    
    user = get_user(user_id)
    
    if user is None:
        products = get_rand_items(count)
        return jsonify({"products": products})
    
    items = get_items_ids()
    top_items = recommande(user_id, items, count)
    top_items = [item[0] for item in top_items]
    products = get_items(top_items)

    return jsonify({"products": products})

if __name__ == '__main__':
    app.run(debug=True)
