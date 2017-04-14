"""User API tests."""
from app import db, create_app
from app.main.models import BlogPost

from internal.test import APITestCase
from internal.test.factories.user import UserFactory
from internal.test.factories.blog import BlogFactory

import json

user_factory = UserFactory()
blogpost_factory = BlogFactory()


class BlogAPITests(APITestCase):
    """User API tests."""

    def setUp(self):
        """Pass db and create_app to parent setUP method."""
        super(BlogAPITests, self).setUp(db, create_app)

    def test_blogpost_create(self):
        """Test whether a blog post can be created."""
        user = user_factory.new()
        blogpost = blogpost_factory.new()

        # Remove published_at as not needed when creating a post and is not json serialisable
        blogpost.pop('published_at', None)
        # blogpost.pop('author_id', None)

        response = self.client.post(
            '/blog',
            data=json.dumps(blogpost),
            headers={'Content-Type': 'application/json', 'author_id': user['pk']}
        )

        self.assertEqual(response.status_code, 201)
        blogpost_from_db = BlogPost.query.filter_by(
            title=blogpost['title']).first()
        self.assertIsNotNone(blogpost_from_db)
