class Endpoints:

    get_users = '/users'
    get_user = lambda self, user_id: f"/users/{user_id}"