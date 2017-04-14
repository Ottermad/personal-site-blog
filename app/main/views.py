"""Views file."""
from flask import Blueprint, request

from .models import *
from .view_functions import blog_post_create

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/")
def index():
    """Index Route."""
    return "Index"


@main_blueprint.route("/blog", methods=("POST",))
def user_create_or_list():
    """Create a blog post or list them."""
    if request.method == "POST":
        return blog_post_create(request)
