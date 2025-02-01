
from functools import wraps
from flask import request, jsonify
from .config import Config

def api_key_required(f):
    """
    Decorator to enforce API key authentication.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        if not api_key or api_key != Config.API_KEY:
            return jsonify({'message': 'Invalid or missing API key'}), 401
        return f(*args, **kwargs)
    return decorated