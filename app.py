from flask import Flask, request, jsonify, send_from_directory
import threading
import time
import random

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/api/swap', methods=['POST'])
def swap():
    data = request.json
    thread = threading.Thread(target=perform_swap, args=(data,))
    thread.daemon = True
    thread.start()
    return jsonify({"success": True, "message": "Swap process started..."})

def perform_swap(data):
    try:
        print(f"[{time.strftime('%H:%M:%S')}] Swap started: {data.get('session1')} -> {data.get('session2')}")
        time.sleep(3)  # Simulate work
        print("✅ Swap completed (simulation)")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    print("🚀 motolov Swapper Running on Render")
    app.run(host='0.0.0.0', port=5000)