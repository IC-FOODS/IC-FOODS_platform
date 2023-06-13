from django.conf import settings
from tapipy.tapis import Tapis
import requests


def is_logged_in(request):
    """
    Check whether the current session contains a valid login;
    If so: return True, username, roles
    Otherwse: return False, None, None
    """
    if 'username' in request.session:
        return True, request.session['username'], request.session['roles']
    return False, None, None


def get_username(token):
    """
    Validate a Tapis JWT, `token`, and resolve it to a username.
    """
    headers = {'Content-Type': 'text/html'}
    # call the userinfo endpoint
    url = f"{settings.TAPIS_API_BASE}/v3/oauth2/userinfo"
    headers = {'X-Tapis-Token': token}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        username = response.json()['result']['username']
    except Exception as e:
        raise Exception(f"Error looking up token info; debug: {e}")
    return username


def add_user_to_session(request, username, token):
    """
    Add a user's identity and Tapis token to the session.
    Also, look up users roles in Tapis and add those to the session.
    The list of roles are returned.
    """
    request.session['username'] = username
    request.session['token'] = token
    # also, look up user's roles
    t = Tapis(base_url=settings.TAPIS_API_BASE, access_token=token)
    try:
        result = t.sk.getUserRoles(user=username, tenant="icicle")
        request.session['roles'] = result.names
    except Exception as e:
        raise Exception(f"Error getting user's roles; debug: {e}")
    return result.names


def clear_session(request):
    """
    Remove all data on the session; this function is called on logout.
    """
    request.session.pop('username', None)
    request.session.pop('token', None)
    request.session.pop('roles', None)
