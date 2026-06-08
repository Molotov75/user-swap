from flask import Flask, send_from_directory, request, jsonify
import threading
import time

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    key = data.get('key')
    if key in ["Molotov", "molotov"]:
        return jsonify({"success": True, "message": "Admin Access"})
    if len(key) > 5:
        return jsonify({"success": True, "message": "Key Valid"})
    return jsonify({"success": False, "message": "Invalid Key"})

@app.route('/api/swap', methods=['POST'])
def swap():
    data = request.json
    thread = threading.Thread(target=lambda: print("Swap started"))
    thread.start()
    return jsonify({"success": True, "message": "Swap started"})

if __name__ == '__main__':
    print("🚀 motolov Swapper Running")
    app.run(host='0.0.0.0', port=5000)
