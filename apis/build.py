# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c)  2018/11/30 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

from flask_restplus import Namespace, Resource, fields, reqparse

from core.build import Build as BuildClass


api = Namespace("build", description="Build Image")

buildModel = api.model("BuildModel", {
    'step' : fields.Integer(required=True, description="步数"),
    'step_content' : fields.List(fields.String, required=True, description="步数内容"),
    'message' : fields.String(required=True, description='信息'),
    'succeed' : fields.Boolean(required=True, description="是否完成")
})

@api.route('/<key>')
class Build(Resource):
    builder = BuildClass()
    @api.marshal_with(buildModel)
    def get(self, key):
        """获取编译项信息"""
        data = self.builder.get_build(key)
        if data:
            return data
        api.abort(404, 'not fund build info')