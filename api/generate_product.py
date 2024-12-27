from typing import List, Tuple
import random

def generate_product(id, score: float=None):
    return {
        'id': id,
        'title': f'Title of {id}',
        'images': [],
        'price': random.randint(100, 10_000) * 0.01,
        'rating': random.randint(1, 5),
        'description': f'Description of item {id}',
        'category': f'Category {round(id % 100)}',
        'discountPercentage': random.randint(1, 50),
        'score': None if score is None else str(score)
    }

def generate_products(ids):
    return [generate_product(i) for i in ids]

def generate_products_score(ids_scores: List[Tuple[int, float]]):
    return [generate_product(i[0], i[1]) for i in ids_scores]
