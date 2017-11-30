from mezzanine.blog.models import BlogPost
from mezzanine import template

register = template.Library()


@register.as_tag
def blog_news(limit=5):
    """
    Put a list of blog posts with the attribute "News=True" into the template context.
    """
    blog_posts = BlogPost.objects.published()
    blog_posts = blog_posts.filter(news=True)
    return list(blog_posts[:limit])
