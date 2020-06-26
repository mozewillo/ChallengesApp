from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from challenges.models import Challenge


def showChallenges(request):
    challenges_list = Challenge.objects.all()
    return render(request, 'challenges/challenges.html', locals())


def ajaxIncrement(request):
    challenge = get_object_or_404(Challenge, pk=request.GET['id'])
    challenge.counter = challenge.counter + 1
    challenge.save()
    return HttpResponse(challenge.counter)


