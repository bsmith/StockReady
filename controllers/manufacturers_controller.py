from flask import Blueprint, render_template, request, url_for, redirect

from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

# RESTful CRUD Routes
# INDEX   — GET '/manufacturers'
# NEW     — GET '/manufacturers/new'
# CREATE  — POST '/manufacturers'
# SHOW    — GET '/manufacturers/<id>'
# EDIT    — GET '/manufacturers/<id>/edit'
# UPDATE  — PUT '/manufacturers/<id>'
# DELETE  — DELETE '/manufacturers/<id>'

# Not needed for MVP
# @manufacturers_blueprint.route('/manufacturers/')
# def manufacturers():
#     all_manufacturers = manufacturer_repository.select_all()
#     return render_template('manufacturers/index.html.j2', all_manufacturers=all_manufacturers)

@manufacturers_blueprint.route('/manufacturers/new')
def new_manufacturer():
    return render_template('manufacturers/new.html.j2')

def _convert_zero_length_str_to_none(string):
    return None if len(string) == 0 else string

def _validate_manufacturer_form(form):
    validated = {}
    validated['full_name'] = form['full_name']
    validated['short_brand_name'] = form['short_brand_name']
    validated['trade_website'] = _convert_zero_length_str_to_none(form['trade_website'])
    validated['trade_telephone'] = _convert_zero_length_str_to_none(form['trade_telephone'])
    validated['customer_website'] = _convert_zero_length_str_to_none(form['customer_website'])
    validated['customer_telephone'] = _convert_zero_length_str_to_none(form['customer_telephone'])
    return validated

@manufacturers_blueprint.route('/manufacturers', methods=["POST"])
def create_manufacturer():
    validated = _validate_manufacturer_form(request.form)
    new_manufacturer = Manufacturer(**validated)
    manufacturer_repository.save(new_manufacturer)
    return redirect(url_for('.show_manufacturer', id=new_manufacturer.id))

@manufacturers_blueprint.route('/manufacturers/<int:id>')
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/show.html.j2', manufacturer=manufacturer)

@manufacturers_blueprint.route('/manufacturers/<int:id>/edit')
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/edit.html.j2', manufacturer=manufacturer)

@manufacturers_blueprint.route('/manufacturers/<int:id>', methods=["POST"])
def update_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    validated = _validate_manufacturer_form(request.form)
    # merge the validated data into the object
    for key, value in validated.items():
        setattr(manufacturer, key, value)
    manufacturer_repository.update(manufacturer)
    return redirect(url_for('.show_manufacturer', id=manufacturer.id))

@manufacturers_blueprint.route('/manufacturers/<int:id>/delete', methods=["POST"])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect(url_for('.manufacturers'))