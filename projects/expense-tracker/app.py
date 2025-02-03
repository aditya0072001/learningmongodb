from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Configure MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/expenses_db")
client = MongoClient(MONGO_URI)
db = client["expenses_db"]
expenses_collection = db["expenses"]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Expense Tracker API"})

@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.json
    if not data or "amount" not in data or "category" not in data:
        return jsonify({"error": "Invalid request data"}), 400
    
    expense = {
        "amount": data["amount"],
        "category": data["category"],
        "description": data.get("description", ""),
        "date": data.get("date", "")
    }
    expenses_collection.insert_one(expense)
    return jsonify({"message": "Expense added successfully"}), 201

@app.route("/expenses", methods=["GET"])
def get_expenses():
    expenses = list(expenses_collection.find({}, {"_id": 0}))
    return jsonify(expenses)

@app.route("/expenses/<category>", methods=["GET"])
def get_expenses_by_category(category):
    expenses = list(expenses_collection.find({"category": category}, {"_id": 0}))
    return jsonify(expenses)

@app.route("/expenses", methods=["DELETE"])
def delete_expenses():
    expenses_collection.delete_many({})
    return jsonify({"message": "All expenses deleted"})

if __name__ == "__main__":
    app.run(debug=True)