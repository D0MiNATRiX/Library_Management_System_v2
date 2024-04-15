from main import app
from application.models import db, Role

with app.app_context():
    db.create_all()
    admin = Role(id='admin', name='Admin', description='Admin Description')
    db.session.add(admin)
    student = Role(id='student', name='Student', description='Student Description')
    db.session.add(student)
    librarian = Role(id='librarian', name='Librarian', description='Librarian Description')
    db.session.add(librarian)
    try:
        db.session.commit()
    except:
        pass