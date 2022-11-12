from flask import Flask

def create_app():
    app = Flask(__name__)

    # register routes and blueprints
    # app.register_blueprint(example_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    # if Flask debug is enabled, also enable DEBUG-level logging
    if app.debug:
        import logging
        logging.basicConfig(level=logging.DEBUG)
    app.run()