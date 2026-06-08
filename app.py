from flask import Flask, send_from_directory, request, jsonify
import threading
import time

app = Flask(__name__)

# Serve the frontend
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/api/swap', methods=['POST'])
def swap():
    data = request.json
    thread = threading.Thread(target=lambda: print("Swap started for", data))
    thread.start()
    return jsonify({"success": True, "message": "Swap process started..."})

if __name__ == '__main__':
    print("🚀 motolov Swapper Running")
    app.run(host='0.0.0.0', port=5000)
