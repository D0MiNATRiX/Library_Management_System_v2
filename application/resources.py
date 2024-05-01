from flask_restful import Resource, Api, reqparse, marshal_with, fields
from flask_security import auth_required, roles_required
from .models import Book, db

api = Api(prefix='/api')

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name is required and should be a string', required=True)
parser.add_argument('content', type=str, help='Content is required and should be a string', required=True)
parser.add_argument('author', type=str, help='Author Link is required and should be a string', required=True)
parser.add_argument('date_issued', type=str, help='Date Issued is required and should be a string', required=True)
parser.add_argument('return_date', type=str, help='Return Date is required and should be a string', required=True)

book_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'content': fields.String,
    'author': fields.String,
    'date_issued': fields.String,
    'return_date': fields.String
}

class Books(Resource):
    @marshal_with(book_fields)
    @auth_required("token")
    def get(self):
        all_book_fields = Book.query.all()
        return all_book_fields
    
    @auth_required("token")
    @roles_required("librarian")
    def post(self):
        args = parser.parse_args()
        book = Book(name=args.get("name"), content=args.get("content"), author=args.get("author"), date_issued=args.get("date_issued"), return_date=args.get("return_date"))
        db.session.add(book)
        db.session.commit()
        return {"message": "Book Created"}

api.add_resource(Books, '/book')