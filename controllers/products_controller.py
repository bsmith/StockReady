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
    all_manufacturers = manufacturer_repository.select_all()
    all_manufacturers.sort(key=lambda m: m.short_brand_name)
    all_products = product_repository.select_all()
    all_products.sort(key=lambda p: p.id)
    products_by_manufacturer_ids = {} # dictionary of lists
    for product in all_products:
        if product.manufacturer.id not in products_by_manufacturer_ids:
            products_by_manufacturer_ids[product.manufacturer.id] = [product]
        else:
            products_by_manufacturer_ids[product.manufacturer.id].append(product)
    return render_template('products/index.html.j2', all_products=all_products, all_manufacturers=all_manufacturers,
        products_by_manufacturer_ids=products_by_manufacturer_ids)

@products_blueprint.route('/products/new')
def new_product():
    all_product_types = product_type_repository.select_all()
    all_manufacturers = manufacturer_repository.select_all()
    return render_template('products/new.html.j2', all_product_types=all_product_types, all_manufacturers=all_manufacturers)

def _validate_product_form(form):
    validated = {}
    validated['mpn'] = form['mpn']
    validated['manufacturer'] = manufacturer_repository.select(form['manufacturer_id'])
    validated['short_description'] = form['short_description']
    validated['long_description'] = form['long_description']
    if len(validated['long_description']) == 0:
        validated['long_description'] = None
    validated['product_type'] = product_type_repository.select(form['product_type_id'])
    validated['screen_size'] = form['screen_size']
    if len(validated['screen_size']) == 0:
        validated['screen_size'] = None
    validated['stock_on_hand'] = form['stock_on_hand']
    validated['cost_price'] = Decimal(form['cost_price'])
    validated['retail_price'] = Decimal(form['retail_price'])
    return validated

@products_blueprint.route('/products', methods=["POST"])
def create_product():
    validated = _validate_product_form(request.form)
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
    validated = _validate_product_form(request.form)
    # merge the validated data into the object
    for key, value in validated.items():
        setattr(product, key, value)
    product_repository.update(product)
    return redirect(url_for('.show_product', id=product.id))

@products_blueprint.route('/products/<int:id>/delete', methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect(url_for('.products'))