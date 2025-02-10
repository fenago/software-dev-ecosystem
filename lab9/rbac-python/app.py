# app.py
from flask import Flask, jsonify, request
from functools import wraps

# Roles configuration
ROLES_PERMISSIONS = {
    "Admin": ["create", "read", "update", "delete"],
    "Editor": ["create", "read", "update"],
    "Viewer": ["read"]
}

# Mock token-to-role store (for testing only)
TOKEN_ROLE_MAP = {
    "admin_token": "Admin",
    "editor_token": "Editor",
    "viewer_token": "Viewer"
}

app = Flask(__name__)

# Helper function to extract role from a token
def get_user_role_from_token():
    # In real apps, parse and verify a JWT or session.
    # Here, we just read a mock token from the request header.
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    return TOKEN_ROLE_MAP.get(token, None)

# Decorator for requiring a permission
def require_permission(permission):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user_role = get_user_role_from_token()
            if not user_role:
                return jsonify({"message": "No valid token found."}), 401

            if permission not in ROLES_PERMISSIONS.get(user_role, []):
                return jsonify({"message": "Access Denied."}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

@app.route("/create", methods=["POST"])
@require_permission("create")
def create_item():
    return jsonify({"status": "Item created successfully."}), 201

@app.route("/read", methods=["GET"])
@require_permission("read")
def read_items():
    return jsonify({"items": ["Item1", "Item2"]}), 200

@app.route("/update", methods=["PUT"])
@require_permission("update")
def update_item():
    return jsonify({"status": "Item updated successfully."}), 200

@app.route("/delete", methods=["DELETE"])
@require_permission("delete")
def delete_item():
    return jsonify({"status": "Item deleted successfully."}), 200

if __name__ == "__main__":
    app.run(debug=True)