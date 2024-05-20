from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.animal_model import Animal
from views import animal_view

# Importamos el decorador de roles
from utils.decorators import role_required

animal_bp = Blueprint("animal", __name__)


@animal_bp.route("/animals")
@login_required
def list_animals():
    animals = Animal.get_all()
    return animal_view.list_animals(animals)

        @animal_bp.route("/users")
    @login_required
    @role_required("admin")
    def list_users():
        users = User.get_all()
        return user_view.list_users(users)


    @animal_bp.route("/users/create", methods=["GET", "POST"])
    @login_required
    @role_required("admin")
    def create_user():
        if request.method == "POST":
            if current_user.has_role("admin"):
                # Retrieve user data from the form
                username = request.form["username"]
                password = request.form["password"]
                role = request.form["role"]
                
                # Create a new user object
                user = User(username=username, password=password, role=role)
                user.save()
                
                flash("User created successfully", "success")
                return redirect(url_for("animal.list_users"))
            else:
                return jsonify({"message": "Unauthorized"}), 403
        return user_view.create_user()


    @animal_bp.route("/users/<int:id>/update", methods=["GET", "POST"])
    @login_required
    @role_required("admin")
    def update_user(id):
        user = User.get_by_id(id)
        if not user:
            return "User not found", 404
        if request.method == "POST":
            if current_user.has_role("admin"):
                # Retrieve updated user data from the form
                username = request.form["username"]
                password = request.form["password"]
                role = request.form["role"]
                
                # Update the user object
                user.update(username=username, password=password, role=role)
                
                flash("User updated successfully", "success")
                return redirect(url_for("animal.list_users"))
            else:
                return jsonify({"message": "Unauthorized"}), 403
        return user_view.update_user(user)


    @animal_bp.route("/users/<int:id>/delete")
    @login_required
    @role_required("admin")
    def delete_user(id):
        user = User.get_by_id(id)
        if not user:
            return "User not found", 404
        if current_user.has_role("admin"):
            user.delete()
            flash("User deleted successfully", "success")
            return redirect(url_for("animal.list_users"))
        else:
            return jsonify({"message": "Unauthorized"}), 403


    @animal_bp.route("/books")
    @login_required
    def list_books():
        books = Book.get_all()
        return book_view.list_books(books)


    @animal_bp.route("/books/create", methods=["GET", "POST"])
    @login_required
    @role_required("admin")
    def create_book():
        if request.method == "POST":
            if current_user.has_role("admin"):
                # Retrieve book data from the form
                title = request.form["title"]
                author = request.form["author"]
                genre = request.form["genre"]
                
                # Create a new book object
                book = Book(title=title, author=author, genre=genre)
                book.save()
                
                flash("Book created successfully", "success")
                return redirect(url_for("animal.list_books"))
            else:
                return jsonify({"message": "Unauthorized"}), 403
        return book_view.create_book()


    @animal_bp.route("/books/<int:id>/update", methods=["GET", "POST"])
    @login_required
    @role_required("admin")
    def update_book(id):
        book = Book.get_by_id(id)
        if not book:
            return "Book not found", 404
        if request.method == "POST":
            if current_user.has_role("admin"):
                # Retrieve updated book data from the form
                title = request.form["title"]
                author = request.form["author"]
                genre = request.form["genre"]
                
                # Update the book object
                book.update(title=title, author=author, genre=genre)
                
                flash("Book updated successfully", "success")
                return redirect(url_for("animal.list_books"))
            else:
                return jsonify({"message": "Unauthorized"}), 403
        return book_view.update_book(book)


    @animal_bp.route("/books/<int:id>/delete")
    @login_required
    @role_required("admin")
    def delete_book(id):
        book = Book.get_by_id(id)
        if not book:
            return "Book not found", 404
        if current_user.has_role("admin"):
            book.delete()
            flash("Book deleted successfully", "success")
            return redirect(url_for("animal.list_books"))
        else:
            return jsonify({"message": "Unauthorized"}), 403


@animal_bp.route("/animals/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_animal():
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            species = request.form["species"]
            age = int(request.form["age"])
            animal = Animal(name=name, species=species, age=age)
            animal.save()
            flash("Animal creado exitosamente", "success")
            return redirect(url_for("animal.list_animals"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return animal_view.create_animal()


@animal_bp.route("/animals/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_animal(id):
    animal = Animal.get_by_id(id)
    if not animal:
        return "Animal no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            species = request.form["species"]
            age = int(request.form["age"])
            animal.update(name=name, species=species, age=age)
            flash("Animal actualizado exitosamente", "success")
            return redirect(url_for("animal.list_animals"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return animal_view.update_animal(animal)


@animal_bp.route("/animals/<int:id>/delete")
@login_required
@role_required("admin")
def delete_animal(id):
    animal = Animal.get_by_id(id)
    if not animal:
        return "Animal no encontrado", 404
    if current_user.has_role("admin"):
        animal.delete()
        flash("Animal eliminado exitosamente", "success")
        return redirect(url_for("animal.list_animals"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
