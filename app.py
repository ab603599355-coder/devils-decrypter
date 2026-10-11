from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from vodafone import get_vodafone_data
import re
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/check", methods=["POST"])
def check():
    data = request.get_json()
    phone = (data.get("phone") or "").replace(" ", "").replace("-", "")
    if not re.fullmatch(r"01\d{9}", phone):
        return jsonify({"success": False, "error": "رقم غير صحيح. مثال: 01012345678"})
    result = get_vodafone_data(phone)
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)