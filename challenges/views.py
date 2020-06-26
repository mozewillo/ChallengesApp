from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from challenges.models import Challenge
from zadanie1.forms import ChallengeForm


def showChallenges(request):
    """ show all challenges in table also added by form"""
    challenges_list = Challenge.objects.all()
    if request.method == 'POST':
        # add challenge if form is filled properly
        form = ChallengeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') #reload page - avoiding duplication
    else:
        form = ChallengeForm()
    return render(request, 'challenges/challenges.html', locals())


def ajaxIncrement(request):
    challenge = get_object_or_404(Challenge, pk=request.GET['id'])
    challenge.counter = challenge.counter + 1
    challenge.save()
    return HttpResponse(challenge.counter)


