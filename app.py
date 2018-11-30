# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c)  2018/11/30 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from apis import api

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)