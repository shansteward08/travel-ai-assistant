 Travel AI Assistant

1. Install dependencies:
pip install -r requirements.txt

2. Run server:
python -m uvicorn main:app --reload

3. Open Swagger:
http://127.0.0.1:8000/docs

Get all travel packages

Get best travel suggestion based on:
- message
- budget
- travelers


{
  "message": "I want a beach trip",
  "budget": 15000,
  "travelers": 2
}

{
  "suggested_destination": "Goa",
  "price_per_person": 10000,
  "total_price": 20000,
  "message": "Best option is Goa because it fits your budget."
}


AI response is mocked due to API limitations.
Structure supports real AI integration.