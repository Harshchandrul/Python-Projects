import requests

# Open Trivia api = https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean
parameters = {
    "amount": 10,
    "category": 18,
    "difficulty": "medium",
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", parameters)
data = response.json()['results']
question_data = data