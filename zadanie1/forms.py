from django.forms import ModelForm
from challenges.models import Challenge

class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = ('name', 'description', 'start_date', 'duration', 'counter')