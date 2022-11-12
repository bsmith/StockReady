from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

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