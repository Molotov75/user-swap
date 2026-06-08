@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    key = data.get('key')

    # Admin Key (Hidden)
    if key == "Molotov" or key == "molotov":
        return jsonify({"success": True, "message": "Admin Access Granted"})

    # Real KeyAuth Check
    try:
        url = f"https://keyauth.cc/api/1.2/?type=login&key={key}&app=611AM's%20Application&ownerid=unw3tp6AeU&version=1.0&secret=ced6a6d57378fb298a4c7f453cb3720614b3e4ec77cd9c090ea982fa0d5e8508"
        
        response = requests.get(url)
        result = response.json()

        if result.get('success'):
            return jsonify({"success": True, "message": "License Validated"})
        else:
            return jsonify({"success": False, "message": result.get('message', 'Invalid Key')})
    except:
        return jsonify({"success": False, "message": "Connection Error"})
