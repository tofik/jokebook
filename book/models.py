from django.db import models

class Joke(models.Model):

    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rank = models.DecimalField(max_digits=6,decimal_places = 0, default = 1)
    author = models.CharField(max_length=20)
    votes = models.PositiveIntegerField(default=0)

    @models.permalink
    def get_absolute_url(self):
        return ('book.views.details', [str(self.id)])

