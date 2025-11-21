from collections import namedtuple
from itertools import combinations
import timeit
from pprint import pprint

SackItem = namedtuple("SackItem", ["name", "weight", "value"])

def knapsack(capacity, items):
    """
    Rezolvă problema Rucsacului 0/1 prin metoda brute-force (combinări).
    """
    reduced_items = [SackItem(**i) for i in items if i["weight"] <= capacity]

    best_value = 0
    best_weight = 0
    best_solution = [] # Va stoca obiectele SackItem
    
    # Verifică toate combinațiile posibile de elemente (de la cele mai mari la cele mai mici)
    for k in reversed(range(1, len(reduced_items) + 1)):
        for proposal in combinations(reduced_items, k):
            p_weigth = sum(p.weight for p in proposal)
            
            # Dacă greutatea depășește capacitatea, ignoră propunerea
            if p_weigth > capacity:
                continue

            p_value = sum(p.value for p in proposal)
            
            # Dacă valoarea este mai bună, actualizează soluția optimă
            if p_value > best_value:
                best_value = p_value
                best_weight = p_weigth
                best_solution = proposal
                
    # Reconstruiește rezultatul în formatul dicționarului dorit
    return { 
        "capacity": capacity,
        "items": [item._asdict() for item in best_solution],
        "weight": best_weight,
        "value": best_value,
    }

def test_knapsack(knapsack_func):
    items = [
        {"name": "laptop", "weight": 4, "value": 2000},
        {"name": "desk lamp", "weight": 2, "value": 12},
        {"name": "textbook", "weight": 3, "value": 20},
        {"name": "wall clock", "weight": 2, "value": 15},
        {"name": "frozen dinners", "weight": 10, "value": 50},
        {"name": "tablet", "weight": 7, "value": 1400},
        {"name": "smartphone", "weight": 1, "value": 200},
        {"name": "paper", "weight": 2, "value": 5},
        {"name": "laser printer", "weight": 25, "value": 400},
        {"name": "shoes", "weight": 1, "value": 79},
        {"name": "medicine", "weight": 1, "value": 17},
        {"name": "toaster oven", "weight": 5, "value": 129},
    ]
    
    # Exemple de capacități
    print(f"Capacitate 0: {knapsack_func(0, items)}")

    capacity1 = 10  # Capacitate mică
    result1 = knapsack_func(capacity1, items)
    print(f"\nCapacitate {capacity1}:")
    pprint(result1)
    
    capacity2 = 100 
    result2 = knapsack_func(capacity2, items)
    print(f"\nCapacitate {capacity2}:")
    pprint(result2)


if __name__ == '__main__':
    test_knapsack(knapsack_func=knapsack)