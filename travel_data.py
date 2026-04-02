travel_packages = [
    {
        "destination": "Goa",
        "type": "Beach",
        "price_per_person": 10000,
        "number_of_days": 3
    },
    {
        "destination": "Manali",
        "type": "Hill Station",
        "price_per_person": 15000,
        "number_of_days": 5
    },
    {
        "destination": "Jaipur",
        "type": "City",
        "price_per_person": 8000,
        "number_of_days": 2
    },
    {
        "destination": "Kerala",
        "type": "Backwaters",
        "price_per_person": 20000,
        "number_of_days": 6
    }
]


def filter_by_budget(packages, budget):
    if budget:
        return [p for p in packages if p["price_per_person"] <= budget]
    return packages