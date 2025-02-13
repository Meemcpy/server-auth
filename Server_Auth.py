<<<<<<< HEAD
﻿from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# ✅ Secret API Key (Only for Admins who generate keys)
ADMIN_API_KEY = "secret-memcpytest"

# ✅ Storage File (Server-Side Only)
DATA_FILE = "keys.json"

# ✅ Load Keys (Server-Side Only)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def load_keys():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_keys(keys):
    with open(DATA_FILE, "w") as f:
        json.dump(keys, f, indent=4)

# ✅ Generate a New Key (Only for Admins)
@app.route('/generate', methods=['POST'])
def generate_key():
    if request.headers.get("Authorization") != ADMIN_API_KEY:
        return jsonify({"error": "Unauthorized"}), 403

    new_key = os.urandom(4).hex().upper() + "-" + os.urandom(4).hex().upper()
    keys = load_keys()
    keys[new_key] = {"hwid": None}
    save_keys(keys)

    return jsonify({"key": new_key})

# ✅ Validate a Key (Checks If HWID Matches)
@app.route('/validate', methods=['GET'])
def validate_key():
    key = request.args.get("key")
    hwid = request.args.get("hwid")

    if not key or not hwid:
        return jsonify({"error": "Missing key or HWID"}), 400

    keys = load_keys()
    if key in keys:
        if keys[key]["hwid"] is None:
            # ✅ First-time activation (Locks HWID)
            keys[key]["hwid"] = hwid
            save_keys(keys)
            return jsonify({"status": "VALID"})
        elif keys[key]["hwid"] == hwid:
            return jsonify({"status": "VALID"})
        else:
            return jsonify({"status": "HWID_MISMATCH"})
    return jsonify({"status": "INVALID"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
﻿from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# ✅ Secret API Key (Only for Admins who generate keys)
ADMIN_API_KEY = "secret-memcpytest"

# ✅ Storage File (Server-Side Only)
DATA_FILE = "keys.json"

# ✅ Load Keys (Server-Side Only)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def load_keys():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_keys(keys):
    with open(DATA_FILE, "w") as f:
        json.dump(keys, f, indent=4)

# ✅ Generate a New Key (Only for Admins)
@app.route('/generate', methods=['POST'])
def generate_key():
    if request.headers.get("Authorization") != ADMIN_API_KEY:
        return jsonify({"error": "Unauthorized"}), 403

    new_key = os.urandom(4).hex().upper() + "-" + os.urandom(4).hex().upper()
    keys = load_keys()
    keys[new_key] = {"hwid": None}
    save_keys(keys)

    return jsonify({"key": new_key})

# ✅ Validate a Key (Checks If HWID Matches)
@app.route('/validate', methods=['GET'])
def validate_key():
    key = request.args.get("key")
    hwid = request.args.get("hwid")

    if not key or not hwid:
        return jsonify({"error": "Missing key or HWID"}), 400

    keys = load_keys()
    if key in keys:
        if keys[key]["hwid"] is None:
            # ✅ First-time activation (Locks HWID)
            keys[key]["hwid"] = hwid
            save_keys(keys)
            return jsonify({"status": "VALID"})
        elif keys[key]["hwid"] == hwid:
            return jsonify({"status": "VALID"})
        else:
            return jsonify({"status": "HWID_MISMATCH"})
    return jsonify({"status": "INVALID"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 0a0cc2c2ce7960e1c706748290ff9c1527acd1ba
