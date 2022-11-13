from flask import Blueprint, render_template, request, url_for, redirect

from models.product_type import ProductType
import repositories.product_type_repository as product_type_repository

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
    all_product_types = product_type_repository.select_all()
    return render_template('product_types/index.html.j2', all_product_types=all_product_types)

# Not needed for MVP
# @product_types_blueprint.route('/product_types/new')
# def new_product():
#     return render_template('product_types/new.html.j2')

@product_types_blueprint.route('/product_types', methods=["POST"])
def create_product_type():
    name = request.form["name"]
    new_product_type = ProductType(name)
    product_type_repository.save(new_product_type)
    return redirect(url_for('.product_types'))

# Not needed for MVP
# @product_types_blueprint.route('/product_types/<int:id>')
# def show_product(id):
#     # ... product_types_repository.select(id) ...
#     return render_template('product_types/show.html.j2')

@product_types_blueprint.route('/product_types/<int:id>/edit')
def edit_product_type(id):
    product_type = product_type_repository.select(id)
    return render_template('product_types/edit.html.j2', product_type=product_type)

@product_types_blueprint.route('/product_types/<int:id>', methods=["POST"])
def update_product_type(id):
    product_type = product_type_repository.select(id)
    product_type.name = request.form["name"]
    product_type_repository.update(product_type)
    return redirect(url_for('.product_types'))

@product_types_blueprint.route('/product_types/<int:id>/delete', methods=["POST"])
def delete_product_type(id):
    product_type_repository.delete(id)
    return redirect(url_for('.product_types'))