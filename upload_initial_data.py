from main import app, datastore
from application.models import db, Role
from flask_security import hash_password

with app.app_context():
    db.create_all()
    datastore.find_or_create_role(name="admin", description="User is an admin")
    db.session.commit()
    datastore.find_or_create_role(name="librarian", description="User is a librarian")
    db.session.commit()
    datastore.find_or_create_role(name="student", description="User is a student")
    db.session.commit()
    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(email="admin@email.com", password=hash_password("admin"), roles=["admin"])
    if not datastore.find_user(email="librarian@email.com"):
        datastore.create_user(email="librarian@email.com", password=hash_password("librarian"), roles=["librarian"], active=False)
    if not datastore.find_user(email="student1@email.com"):
        datastore.create_user(email="student1@email.com", password=hash_password("student1"), roles=["student"])
    db.session.commit()