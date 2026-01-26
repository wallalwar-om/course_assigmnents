from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    try:
        with open('data.txt', 'r') as file:
            data = json.load(file)

        return jsonify({"data": data})
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    

if __name__ == "__main__":
    app.run(debug=True)