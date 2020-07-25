from flask import Blueprint, g, request, abort, jsonify
from flask_jwt_extended import (
    set_access_cookies, create_access_token, get_jwt_identity,
    create_refresh_token, set_refresh_cookies,
    jwt_refresh_token_required, unset_jwt_cookies
)
from models.db import db
from models.User import User
from flask import current_app
from flask_expects_json import expects_json
from util.roles_required import roles_required
from models.Role import RoleName, Role
import datetime
from email.utils import parseaddr


auth_blueprint = Blueprint('auth', __name__)


auth_schema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['username', 'password']
}


@auth_blueprint.route('/auth', methods=['POST'])
@expects_json(auth_schema)
def login():
    content = g.data

    username = content['username']
    password = content['password']

    user = User.query.filter(
        User.name == username
    ).first()

    if user is None:
        abort(400, 'User not found')
        return

    if not user.is_active:
        abort(403, 'User has been banned')
        return

    if not user.check_password(password):
        abort(400, 'Invalid password')
        return

    at_expires = datetime.timedelta(days=current_app.config['ACCESS_TOKEN_EXPIRES_DAYS'])
    access_token = create_access_token(identity=user.id, expires_delta=at_expires)
    rt_expires = datetime.timedelta(days=current_app.config['REFRESH_TOKEN_EXPIRES_DAYS'])
    refresh_token = create_refresh_token(identity=user.id, expires_delta=rt_expires)
    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)

    return resp


@auth_blueprint.route('/auth', methods=['DELETE'])
def remove_token():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp, 200


@auth_blueprint.route('/auth/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh_token():
    current_user_id = get_jwt_identity()
    access_token = create_access_token(identity=current_user_id)

    resp = jsonify({'refresh': True})
    set_access_cookies(resp, access_token)

    return resp, 200


register_schema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string'},
        'password': {'type': 'string'},
        'email': {'type': 'string'},
        'roles': {
            'type': 'array',
            'items': {
                'type': 'string',
                'enum': [e.name for e in RoleName]
            },
            'minItems': 1
        }
    },
    'required': ['username', 'password']
}


@auth_blueprint.route('/user', methods=['POST'])
@expects_json(register_schema)
@roles_required([RoleName.admin])
def register_user():
    content = g.data
    session = db.create_scoped_session()

    users = session.query(User).all()

    username = content['username']
    if any(user.name == username for user in users):
        session.close()
        abort(400, "User with name = %s already exist" % username)
        return

    email = content['email']
    if '@' not in parseaddr(email)[1]:
        session.close()
        abort(400, "Invalid email")
        return
    if any(user.email == email for user in users):
        session.close()
        abort(400, "User with email = %s already exist" % email)
        return

    roles = list(map(lambda r: Role.get_by_name(r), content['roles']))

    user = User(
        name=username,
        email=email,
        roles=roles
    )

    user.set_password(content['password'])

    session.add(user)

    session.commit()
    session.close()

    return 'ok'
