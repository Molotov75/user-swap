from flask import Flask, request, jsonify, send_from_directory
import threading
import time

app = Flask(__name__)

# Serve the frontend
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    key = data.get('key')
    
    if key in ["Molotov", "molotov"]:
        return jsonify({"success": True, "message": "Admin Access"})
    
    # Simple KeyAuth simulation (you can replace with real later)
    if len(key) > 5:
        return jsonify({"success": True, "message": "Key Valid"})
    return jsonify({"success": False, "message": "Invalid Key"})

@app.route('/api/swap', methods=['POST'])
def swap():
    data = request.json
    thread = threading.Thread(target=perform_swap, args=(data,))
    thread.daemon = True
    thread.start()
    return jsonify({"success": True, "message": "Swap process started..."})

def perform_swap(data):
    print(f"[{time.strftime('%H:%M:%S')}] Swap started for {data.get('session1')} -> {data.get('session2')}")
    time.sleep(3)
    print("✅ Swap simulation completed")

if __name__ == '__main__':
    print("🚀 motolov Swapper Running")
    app.run(host='0.0.0.0', port=5000)
