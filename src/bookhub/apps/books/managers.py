from django.db import models

from treebeard.mp_tree import MP_NodeQuerySet


class CategoryQuerySet(MP_NodeQuerySet):
    def is_public(self):
        return self.filter(is_public=True)


class BookQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(is_public=True)