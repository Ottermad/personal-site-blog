"""Models file."""
import datetime
import markdown2

from app import db


class BlogPost(db.Model):
    """Blog Post model."""

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    markdown = db.Column(db.Text)
    html = db.Column(db.Text)
    author_id = db.Column(db.Integer)
    published = db.Column(db.Boolean, default=False)
    published_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, title, markdown, author_id, published):
        """Constructor."""
        self.title = title
        self.markdown = markdown
        self.html = markdown2.markdown(markdown, extras=["fenced-code-blocks"])
        self.author_id = author_id
        if published:
            self.publish()

    def publish(self):
        """Toogle whether an article is published."""
        self.publish = not self.published
        self.published_at = datetime.datetime.now()

    def to_dict(self):
        """Convert User object to dictionary."""
        return {
            'id': self.pk,
            'title': self.title,
            'markdown': self.markdown,
            'html': self.html,
            'author_id': self.author_id,
            'published': self.published,
            'published_at': self.published_at
        }
