from itertools import groupby
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

def groupby_manufacturer_id(products):
    def keyfunc(product):
        return product.manufacturer.id
    sorted_products = sorted(products, key=keyfunc)
    products_by_manufacturer_id = {} # dictionary of lists
    for key, group in groupby(sorted_products, key=keyfunc):
        products_by_manufacturer_id[key] = list(group)
    return products_by_manufacturer_id

@products_blueprint.route('/products/')
def products():
    all_manufacturers = manufacturer_repository.select_all()
    all_manufacturers.sort(key=lambda m: m.short_brand_name)
    all_products = product_repository.select_all()
    products_by_manufacturer_ids = groupby_manufacturer_id(all_products)
    return render_template('products/index.html.j2',
        filtered=False, filter_msg="",
        manufacturers=all_manufacturers,
        products_by_manufacturer_ids=products_by_manufacturer_ids)

@products_blueprint.route('/products/current_inventory')
def current_inventory():
    all_products = product_repository.select_all()
    def filterfunc(product):
        return not product.should_hide_discontinued_product()
    products_to_show = filter(filterfunc, all_products)
    products_by_manufacturer_ids = groupby_manufacturer_id(products_to_show)

    manufacturers = []
    for manufacturer_id in products_by_manufacturer_ids.keys():
        manufacturers.append(manufacturer_repository.select(manufacturer_id))
    manufacturers.sort(key=lambda m: m.short_brand_name)

    return render_template('products/index.html.j2',
        filtered=True, filter_msg="Current Inventory",
        manufacturers=manufacturers,
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
    validated['discontinued'] = 'discontinued' in form
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
    allow_delete = True
    return render_template('products/edit.html.j2', product=product, all_product_types=all_product_types, all_manufacturers=all_manufacturers, allow_delete=allow_delete)

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