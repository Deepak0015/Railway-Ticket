from flask import Blueprint, render_template, request, jsonify

admin_bp = Blueprint('admin_bp', __name__)

# Valid admin credentials
VALID_ADMINS = {
    "admin": "admin123",
    "mariselvam": "mariselvam007"
}

@admin_bp.route('/', methods=['GET'])
def admin_login_page():
    return render_template('adminlogin.html')

@admin_bp.route('/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({
            "success": False,
            "message": "Admin username and password are required"
        }), 400
    
    if username in VALID_ADMINS and VALID_ADMINS[username] == password:
        return jsonify({
            "success": True,
            "message": "Admin login successful",
            "redirect": "/admin/dashboard"
        })
    else:
        return jsonify({
            "success": False,
            "message": "Invalid admin credentials"
        }), 401

@admin_bp.route('/dashboard')
def admin_dashboard():
    return render_template('admin.html')