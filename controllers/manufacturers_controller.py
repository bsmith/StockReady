from flask import Blueprint, render_template

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
#     # ... manufacturers_repository.select_all() ...
#     return render_template('manufacturers/index.html.j2')

@manufacturers_blueprint.route('/manufacturers/new')
def new_product():
    return render_template('manufacturers/new.html.j2')

@manufacturers_blueprint.route('/manufacturers', methods=["POST"])
def create_product():
    # ... manufacturers_repository.save(product) ...
    raise NotImplementedError()

@manufacturers_blueprint.route('/manufacturers/<int:id>')
def show_product(id):
    # ... manufacturers_repository.select(id) ...
    return render_template('manufacturers/show.html.j2')

@manufacturers_blueprint.route('/manufacturers/<int:id>/edit')
def edit_product(id):
    # ... manufacturers_repository.select(id) ...
    return render_template('manufacturers/edit.html.j2')

@manufacturers_blueprint.route('/manufacturers/<int:id>', methods=["POST"])
def update_product(id):
    # ... manufacturers_repository.update(product) ...
    raise NotImplementedError()

@manufacturers_blueprint.route('/manufacturers/<int:id>/delete', methods=["POST"])
def delete_product(id):
    # ... manufacturers_repository.delete(id) ...
    raise NotImplementedError()