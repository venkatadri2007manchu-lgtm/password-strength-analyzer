from flask import Flask, request, jsonify, render_template_string
from analyzer import evaluate_password
from generator import generate_suggestions
from db import init_db, is_reused_password, save_password_hash

app = Flask(__name__)
init_db()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Password Strength Analyzer</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; }
        input, button { padding: 10px; width: 100%; margin-top: 10px; box-sizing: border-box; }
        .result { background: #f4f4f4; padding: 15px; border-radius: 5px; margin-top: 20px; }
    </style>
</head>
<body>
    <h2>Password Strength Analyzer</h2>
    <input type="password" id="password" placeholder="Enter password to test...">
    <button onclick="analyze()">Analyze Password</button>
    <div id="output" class="result" style="display:none;"></div>

    <script>
        async function analyze() {
            const pwd = document.getElementById('password').value;
            const res = await fetch('/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({user_id: 'browser_user', password: pwd})
            });
            const data = await res.json();
            document.getElementById('output').style.display = 'block';
            document.getElementById('output').innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE)

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