from flask import Blueprint, render_template

products_blueprint = Blueprint("products", __name__)

# RESTful CRUD Routes
# INDEX   — GET '/products'
# NEW     — GET '/products/new'
# CREATE  — POST '/products'
# SHOW    — GET '/products/<id>'
# EDIT    — GET '/products/<id>/edit'
# UPDATE  — PUT '/products/<id>'
# DELETE  — DELETE '/products/<id>'

@products_blueprint.route('/products/')
def products():
    # ... products_repository.select_all() ...
    return render_template('products/index.html.j2')

@products_blueprint.route('/products/new')
def new_product():
    return render_template('products/new.html.j2')

@products_blueprint.route('/products', methods=["POST"])
def create_product():
    # ... products_repository.save(product) ...
    raise NotImplementedError()

@products_blueprint.route('/products/<int:id>')
def show_product(id):
    # ... products_repository.select(id) ...
    return render_template('products/show.html.j2')

@products_blueprint.route('/products/<int:id>/edit')
def edit_product(id):
    # ... products_repository.select(id) ...
    return render_template('products/edit.html.j2')

@products_blueprint.route('/products/<int:id>', methods=["POST"])
def update_product(id):
    # ... products_repository.update(product) ...
    raise NotImplementedError()

@products_blueprint.route('/products/<int:id>/delete', methods=["POST"])
def delete_product(id):
    # ... products_repository.delete(id) ...
    raise NotImplementedError()