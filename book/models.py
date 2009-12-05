from django.db import models

class Joke(models.Model):

    content = models.TextField()
    created = models.TimeField(auto_now_add=True)

    @models.permalink
    def get_absolute_url(self):
        return ('book.views.details', [str(self.id)])

