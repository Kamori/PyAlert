#!/usr/bin/env python

from flask import Flask, g, render_template, request, url_for, redirect, \
    current_app, session, make_response
import traceback
import sys



def register_blueprints(app):
    return None


def register_extensions(app):
    return None


def register_errorhandlers(app):
    @app.errorhandler(404)
    def notfound(error):
        error = "{0}".format(error), 404
        return error

    @app.errorhandler(403)
    def denied(error):
        return error

    @app.errorhandler(Exception)
    def servererror(error):
        trace = traceback.format_exc()
        return str(trace), 500

    return None


def register_globals(app):
    # Defining variables with g must be set in the correct context
    # The decorator before_request will allow this.
    # App must be defined before the decorator can be used, thus the
    # nested function. Plus allows this func to define other future
    # settings
    @app.before_request
    def set_global():
        pass

    return None


def register_routes(app):
    # These are routes that do not belong as part of a blueprint
    # Should these grow expect to abstract them out to their own file

    @app.route('/')
    def index():
       return "Hello PyAlert"


def configure(**kwargs):
    app = Flask(__name__, template_folder='resources/templates',
                static_folder='resources/static')
    # app.config.from_object('src.config')

    # Lets register some defaults
    register_errorhandlers(app)
    register_blueprints(app)
    register_globals(app)
    register_routes(app)
    register_extensions(app)

    return app


if __name__ == '__main__':
    print("Reference README")
    raise SystemExit
