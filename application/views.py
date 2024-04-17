from flask import current_app as app, jsonify
from flask_security import auth_required, roles_required
from .models import User, db

@app.get('/')
def home():
    return 'Hello World'

@app.get('/admin')
@auth_required("token")
@roles_required("admin")
def admin():
    return 'Welcome Admin'

@app.get('/activate/librarian')
@auth_required("token")
@roles_required("admin")
def activate_librarian():
    librarian = User.query.get(2)
    if not librarian or "librarian" not in librarian.roles:
        return jsonify({"message":"Librarian Not Found"}), 404
    librarian.active = True
    db.session.commit()
    return jsonify({"message":"User Activated"})