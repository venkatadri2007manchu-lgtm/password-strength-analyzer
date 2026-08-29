from flask import Flask, request, jsonify
from analyzer import evaluate_password
from generator import generate_suggestions
from db import init_db, is_reused_password, save_password_hash

app = Flask(__name__)
init_db()

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json or {}
    user_id = data.get("user_id", "demo_user")
    password = data.get("password", "")

    if not password:
        return jsonify({"error": "Password is required"}), 400

    reused = is_reused_password(user_id, password)
    evaluation = evaluate_password(password)
    suggestions = generate_suggestions(password)

    if not reused:
        save_password_hash(user_id, password)

    return jsonify({
        "evaluation": evaluation,
        "suggestions": suggestions,
        "is_reused": reused
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)