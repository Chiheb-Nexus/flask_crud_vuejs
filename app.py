#
# Application main views
#

from random import randint
from config import CURRENT_CONFIG
from flask import Flask, render_template, jsonify
from flask.views import MethodView
from flask_cors import CORS


application = Flask(__name__)
application.config.from_object(CURRENT_CONFIG)
CORS(application, resources={r'/*': {'origins': '*'}})


class HomeView(MethodView):
    """Home View"""
    def get(self):
        context = {'title': 'Home'}
        return render_template('home.html', **context)


class RandomValuesView(MethodView):
    """Return random values"""
    def get(self):
        chars = [chr(randint(65, 90)) for _ in range(1, 20)]
        nums = [(chr(randint(48, 57)), True if k % 2 == 0 else False) for k in range(1, 20)]
        return jsonify({'data': [{'key': k, 'value': v, 'isPrimary': z } for k, (v, z) in zip(chars, nums)]})



application.add_url_rule('/', view_func=HomeView.as_view('home'))
application.add_url_rule('/random/', view_func=RandomValuesView.as_view('random'))
