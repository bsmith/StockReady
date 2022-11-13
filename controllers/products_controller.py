from decimal import Decimal

from flask import Blueprint, render_template, request, url_for, redirect

from models.product import Product
import repositories.product_type_repository as product_type_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

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
    all_products = product_repository.select_all()
    return render_template('products/index.html.j2', all_products=all_products)

@products_blueprint.route('/products/new')
def new_product():
    all_product_types = product_type_repository.select_all()
    all_manufacturers = manufacturer_repository.select_all()
    return render_template('products/new.html.j2', all_product_types=all_product_types, all_manufacturers=all_manufacturers)

def _validate_product_form(request):
    validated = {}
    validated['mpn'] = request['mpn']
    validated['manufacturer'] = manufacturer_repository.select(request['manufacturer_id'])
    validated['short_description'] = request['short_description']
    validated['long_description'] = request['long_description']
    if len(validated['long_description']) == 0:
        validated['long_description'] = None
    validated['product_type'] = product_type_repository.select(request['product_type_id'])
    validated['screen_size'] = request['screen_size']
    validated['stock_on_hand'] = request['stock_on_hand']
    validated['cost_price'] = Decimal(request['cost_price'])
    validated['retail_price'] = Decimal(request['retail_price'])
    return validated

@products_blueprint.route('/products', methods=["POST"])
def create_product():
    validated = _validate_product_form(request)
    new_product = Product(**validated)
    product_repository.save(new_product)
    return redirect(url_for('.show_product', id=new_product.id))

@products_blueprint.route('/products/<int:id>')
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/show.html.j2', product=product)

@products_blueprint.route('/products/<int:id>/edit')
def edit_product(id):
    product = product_repository.select(id)
    all_product_types = product_type_repository.select_all()
    all_manufacturers = manufacturer_repository.select_all()
    return render_template('products/edit.html.j2', product=product, all_product_types=all_product_types, all_manufacturers=all_manufacturers)

@products_blueprint.route('/products/<int:id>', methods=["POST"])
def update_product(id):
    product = product_repository.select(id)
    validated = _validate_product_form(request)
    # merge the validated data into the object
    for key, value in validated.items:
        setattr(product, key, value)
    product_repository.update(product)
    return redirect(url_for('.show_product', id=new_product.id))

@products_blueprint.route('/products/<int:id>/delete', methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect(url_for('.products'))