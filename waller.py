# -*- coding: utf-8 -*-
"""Create an application instance."""
import sys

from flask.helpers import get_debug_flag
from walle.app import create_app
from walle.config.settings_dev import DevConfig
from walle.config.settings_test import TestConfig
from walle.config.settings_prod import ProdConfig

# 默认Walle配置
CONFIG = DevConfig if get_debug_flag() else ProdConfig

# 脚本执行参数指定缓存
if len(sys.argv) > 2 and sys.argv[2] == 'test':
    CONFIG = TestConfig

# 创建Flask APP
app = create_app(CONFIG)
