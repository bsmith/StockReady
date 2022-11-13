from flask import Flask, render_template

from controllers.products_controller import products_blueprint
from controllers.manufacturers_controller import manufacturers_blueprint
from controllers.product_types_controller import product_types_blueprint

def create_app():
    app = Flask(__name__)

    # https://stackoverflow.com/questions/46944596/is-autoescape-default-in-jinja2-flask
    app.jinja_options["autoescape"] = lambda _: True

    # register routes and blueprints
    app.register_blueprint(products_blueprint)
    app.register_blueprint(manufacturers_blueprint)
    app.register_blueprint(product_types_blueprint)

    @app.route('/')
    def home():
        return render_template('index.html.j2', title="Homepage")

    # if Flask debug is enabled, also enable DEBUG-level logging
    if app.debug:
        print("Enabling DEBUG log level")
        import logging
        logging.basicConfig()
        logging.getLogger('db.run_sql').setLevel(logging.DEBUG)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()