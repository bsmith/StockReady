from flask import Blueprint, render_template

product_types_blueprint = Blueprint("product_types", __name__)

# RESTful CRUD Routes
# INDEX   — GET '/product_types'
# NEW     — GET '/product_types/new'
# CREATE  — POST '/product_types'
# SHOW    — GET '/product_types/<id>'
# EDIT    — GET '/product_types/<id>/edit'
# UPDATE  — PUT '/product_types/<id>'
# DELETE  — DELETE '/product_types/<id>'

@product_types_blueprint.route('/product_types/')
def product_types():
    # ... product_types_repository.select_all() ...
    return render_template('product_types/index.html.j2')

# Not needed for MVP
# @product_types_blueprint.route('/product_types/new')
# def new_product():
#     return render_template('product_types/new.html.j2')

@product_types_blueprint.route('/product_types', methods=["POST"])
def create_product():
    # ... product_types_repository.save(product) ...
    raise NotImplementedError()

# Not needed for MVP
# @product_types_blueprint.route('/product_types/<int:id>')
# def show_product(id):
#     # ... product_types_repository.select(id) ...
#     return render_template('product_types/show.html.j2')

@product_types_blueprint.route('/product_types/<int:id>/edit')
def edit_product(id):
    # ... product_types_repository.select(id) ...
    return render_template('product_types/edit.html.j2')

@product_types_blueprint.route('/product_types/<int:id>', methods=["POST"])
def update_product(id):
    # ... product_types_repository.update(product) ...
    raise NotImplementedError()

@product_types_blueprint.route('/product_types/<int:id>/delete', methods=["POST"])
def delete_product(id):
    # ... product_types_repository.delete(id) ...
    raise NotImplementedError()