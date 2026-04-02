from fastapi import FastAPI, Query
from dotenv import load_dotenv

from travel_data import travel_packages, filter_by_budget
from schemas import TravelRequest

load_dotenv()

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Travel AI Assistant Running"}


@app.get("/packages")
def get_packages(budget: int = Query(default=None)):
    filtered = filter_by_budget(travel_packages, budget)
    return {"packages": filtered}


@app.post("/travel-chat")
def travel_chat(request: TravelRequest):
    # Step 1: Filter packages
    filtered_packages = filter_by_budget(travel_packages, request.budget)

    # Step 2: Mock AI logic
    if filtered_packages:
        best_package = filtered_packages[0]
        ai_output = f"Best option is {best_package['destination']} because it fits your budget."
        price_per_person = best_package["price_per_person"]
        destination = best_package["destination"]
    else:
        ai_output = "No packages available for your budget."
        price_per_person = 0
        destination = None

    # Step 3: Calculate total price
    total_price = None
    if request.travelers:
        total_price = price_per_person * request.travelers

    # Step 4: Return response
    return {
        "suggested_destination": destination,
        "price_per_person": price_per_person,
        "total_price": total_price,
        "message": ai_output
    }