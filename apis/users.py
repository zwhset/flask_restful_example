# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    Users API

    :copyright: (c)  2018/11/30 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""
import uuid

from flask_restplus import Namespace, Resource, fields, reqparse

api = Namespace("users", description="Users API")

userModel = api.model('UserModel', {
    'id': fields.String(required=True, description='用户ID'),
    'username': fields.String(required=True, description='用户名')
})

publicModel = api.model('publicModel', {
    'code': fields.Integer(description="状态码", default=0),
    'message': fields.String(description='信息', default="Success")
})

parser = reqparse.RequestParser()
parser.add_argument("username", required=True, type=str, help="字段username不是字符串")

USERS = [
    {
        "username": "john",
        "id": "5d9f34caf48711e885156a0003a72bb0"
    },
    {
        "username": "zwhset",
        "id": "65490fd4f48711e8b9126a0003a72bb0"
    },
    {
        "username": "l0set",
        "id": "6821e387f48711e8a07b6a0003a72bb0"
    }
]

@api.route('/')
class Users(Resource):
    @api.marshal_list_with(userModel)
    def get(self):
        """列出所有用户"""
        return USERS

    @api.marshal_with(userModel)
    @api.param("username", "用户名")
    def post(self):
        """创建用户"""
        args = parser.parse_args()
        user = dict(
            username=args.get('username', None),
            id = uuid.uuid1().get_hex()
        )
        USERS.append(user)
        return user


@api.route('/<id>')
@api.param("id", '用户ID')
@api.response(404, '未找到用户')
class User(Resource):
    @api.marshal_with(userModel)
    def get(self, id):
        """获取ID的用户信息"""
        for user in USERS:
            if user.get('id', None) == id:
                return user
        api.abort(404, 'not fund user')

    @api.param("username", "用户名")
    @api.marshal_with(userModel)
    def put(self, id):
        """通过ID更新用户信息"""
        args = parser.parse_args()
        username = args.get('username', None)
        for user in USERS:
            if user.get('id', None) == id:
                user['username'] = username
                return user
        api.abort(404, 'not fund user')

    @api.marshal_with(publicModel)
    def delete(self, id):
        for i, user in enumerate(USERS):
            if user.get('id', None) == id:
                del USERS[i]
                return
        api.abort(404, 'not fund user')
