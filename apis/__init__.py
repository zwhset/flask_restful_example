# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    APIs init

    :copyright: (c)  2018/11/30 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

from flask_restplus import Api

from users import api as user_ns
from build import api as build_ns

api = Api(
    title="flask restplus example API",
    version='1.0',
    description='User description'
)

api.add_namespace(user_ns, path='/api/users')
api.add_namespace(build_ns, path='/api/cluster/build')