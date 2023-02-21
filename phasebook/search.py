from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route('')
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    if args:
        filtered_user = []
        filted_id = []
        if 'id' in args:
            for user in USERS:
                if args['id'] == user['id']:
                    filtered_user.append(user)
                    filted_id.append(user['id'])

        if 'name' in args:
            for user in USERS:
                if user['id'] not in filted_id:
                    if args['name'].lower() in user['name'].lower():
                        filtered_user.append(user)
                        filted_id.append(user['id'])

        if 'age' in args:
            for user in USERS:
                if user['id'] not in filted_id:
                    if (int(args['age']) - 1) <= int(user['age']) <= (int(args['age']) + 1):
                        filtered_user.append(user)
                        filted_id.append(user['id'])

        if 'occupation' in args:
            for user in USERS:
                if user['id'] not in filted_id:
                    if args['occupation'] in args['occupation']:
                        filtered_user.append(user)
                        filted_id.append(user['id'])

        return filtered_user

    else:
        return USERS
