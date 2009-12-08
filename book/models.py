from django.db import models

class Joke(models.Model):

    content = models.TextField()
    created = models.TimeField(auto_now_add=True)
    rank = models.DecimalField(max_digits = 1, decimal_places = 0, default = 1)

    @models.permalink
    def get_absolute_url(self):
        return ('book.views.details', [str(self.id)])

