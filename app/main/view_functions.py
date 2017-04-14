"""Functions which map to views."""
from app import db

from flask import jsonify

from internal.errors import HTTPException
from internal.helper import (
    json_from_request,
    check_keys
)

from .models import BlogPost


def blog_post_create(request):
    """Create a blog post."""
    json_data = json_from_request(request)

    expected_keys = [
        "title",
        "markdown",
        "published",
    ]

    check_keys(expected_keys, json_data)

    blogpost = BlogPost(
        title=json_data['title'],
        markdown=json_data['markdown'],
        published=json_data['published'],
        author_id=request.headers.get('user-id')
    )

    db.session.add(blogpost)
    db.session.commit()

    return jsonify(blogpost.to_dict()), 201
