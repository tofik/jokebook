from jokebook.book.models import Joke
from django.forms import ModelForm

class NewJokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ('content','author',)
