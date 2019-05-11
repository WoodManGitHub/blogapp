from django.contrib.syndication.views import Feed
from .models import Post

class AllPostRss(Feed):
    title = 'Django blog RSS'
    link = '/'
    description = "Django RSS"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.content
