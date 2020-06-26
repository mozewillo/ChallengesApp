from django.shortcuts import render

# Create your views here.
from challenges.models import Challenge


def showChallenges(request):
    challenges_list = Challenge.objects.all()
    return render(request, 'challenges.challenges.html', locals())

