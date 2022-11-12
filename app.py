from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # https://stackoverflow.com/questions/46944596/is-autoescape-default-in-jinja2-flask
    app.jinja_options["autoescape"] = lambda _: True

    # register routes and blueprints
    # app.register_blueprint(example_blueprint)

    @app.route('/')
    def home():
        return render_template('index.html.j2', title="Homepage")

    return app

if __name__ == "__main__":
    app = create_app()
    # if Flask debug is enabled, also enable DEBUG-level logging
    if app.debug:
        import logging
        logging.basicConfig(level=logging.DEBUG)
    app.run()