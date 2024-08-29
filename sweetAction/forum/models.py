from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager


from django.utils.text import slugify


class Board(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=400)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics', default=1)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=400)
    # set and enforce one-to-one post to topic relationship using a foreign key
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts', default=1)
    content = HTMLField()
    categories = models.ManyToManyField('Category')
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    hitcount_tracker = GenericRelation(HitCount, object_id_field='object_pk',
        related_query_name='hitcount_tracker_relation'
    )
    tags = TaggableManager()
# configure delete


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class User(models.Model):
    fullname = models.CharField(max_length=40, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='users', default=1)
    avatar = models.ImageField(upload_to='avatarimages/', max_length=100, blank=True, null=True)
    bio = HTMLField()
    rizz = models.IntegerField(default=0)
    slug = models.SlugField(max_length=400, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.fullname


class Category(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)

    class Meta:
        # specifying the plural use of the term
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title