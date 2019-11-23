"""
The flask application package.
"""

from flask import Flask
import os
app = Flask(__name__,static_url_path='/static')


import clippr.views
