import json
import os
import sys
from hashlib import sha256

DEFAULT_FEATURES = [
    {"code": "Device:All",            "description": "Support for all Nipper network devices"},
    {"code": "Extension:All",         "description": "Support for all Nipper capability extensions"},
    {"code": "Feature:All",           "description": "Everything"},
    {"code": "Report:All",            "description": "All Reports"},
    {"code": "Mitigation Script:All", "description": "Support for all types of mitigation scripts"},
    {"code": "Save:All",              "description": "Support for all save formats"},
]

def load_json():
    path = "activation-request.nlr"
    if not os.path.isfile(path):
        print(f"[-] Error: File not found: {path}")
        sys.exit(1)
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("[-] Error: Failed to parse JSON in")
        sys.exit(1)

def write_json(obj):
    path = "activation-response.nlr"
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2)
    print(f"[+]  Wrote activation response to '{path}'")

def compute_hash(secret_key, body_obj):
    body_bytes = json.dumps(body_obj, separators=(',', ':')).encode('utf-8')
    combined = secret_key.encode('utf-8') + body_bytes
    digest = sha256(combined).hexdigest()
    print(f"[+]  Computed response hash: {digest}")
    return digest

def build_response(request, secret_key):
    hdr = request.get('headers', {})
    for field in ('activation_code', 'serial_number', 'transaction_id'):
        if field not in hdr:
            print(f"[-] Error: Missing '{field}' in request headers")
            sys.exit(1)

    resp = {
        "body": {
            "activation_code": hdr['activation_code'],
            "error_code": 0,
            "features": DEFAULT_FEATURES,
            "serial_number": hdr['serial_number'],
            "status": {
                "description": "Working license",
                "name": "Live"
            },
            "term": {
                "period": 9999,
                "start_date": "2025-01-01"
            },
            "transaction_id": hdr['transaction_id'],
            "type": {},
            "usage": [],
            "usage_allowance": 999
        },
        "headers": {
            "Content-Type": "application/json",
            "activation_code": hdr['activation_code'],
            "serial_number": hdr['serial_number'],
            "transaction_id": hdr['transaction_id'],
            "hash": "" 
        }
    }

    resp['headers']['hash'] = compute_hash(secret_key, resp['body'])
    return resp

def main():

    print("[?] Loading request…")
    request = load_json()

    print("[?] Building activation response…")
    response = build_response(request, "1234abcd5678fedc")

    print("[?] Writing output…")
    write_json(response)

    print("[+] Done.")

if __name__ == "__main__":
    main()