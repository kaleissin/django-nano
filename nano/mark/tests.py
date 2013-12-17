from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User

from nano.mark.models import MarkedMixin, Mark, MarkType

class Item(MarkedMixin):
    slug = models.SlugField(max_length=30)

class MarkTypeTest(TestCase):

    def setUp(self):
        self.fave = MarkType.objects.create(name='Fave')
        self.flag = MarkType.objects.create(name='Flag')
        self.scrambled = MarkType.objects.create(name='Scrambled')
        self.removed = MarkType.objects.create(name='Removed')

    def test_str(self):
        self.assertEqual(str(self.fave), 'Fave')

class MarkTest(TestCase):

    def setUp(self):
        self.fave = MarkType.objects.create(name='Fave')
        self.flag = MarkType.objects.create(name='Flag')
        self.scrambled = MarkType.objects.create(name='Scrambled')
        self.removed = MarkType.objects.create(name='Removed')
        self.item = Item.objects.create(slug='test')
        self.user = User.objects.create(username='user1')

    def test_str(self):
        item = Mark(marktype=self.fave, marked_by=self.user, object_pk=str(self.item.pk))
        self.assertEqual(str(item), "%s have marked %s" % (self.user, item.content_object))

class MarkedMixinTest(TestCase):
    def setUp(self):
        self.fave = MarkType.objects.create(name='Fave')
        self.flag = MarkType.objects.create(name='Flag')
        self.scrambled = MarkType.objects.create(name='Scrambled')
        self.removed = MarkType.objects.create(name='Removed')
        self.item = Item.objects.create(slug='test')
        self.user = User.objects.create(username='user1')
 
    def test_faved(self):
        self.item 
