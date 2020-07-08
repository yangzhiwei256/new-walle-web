# -*- coding: utf-8 -*-
"""Create an application instance."""
import sys
import os
from flask.helpers import get_debug_flag
from walle.app import create_app
from walle.config import envrionment

# 创建Flask APP
configName = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(envrionment[configName])
