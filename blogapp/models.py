from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

class Tag(models.Model):
    name = models.CharField(max_length=50)
	
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
	
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    viewnum = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.viewnum += 1
        self.save(update_fields=['viewnum'])
    
    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.content))[:54]

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
	
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-created_time']
