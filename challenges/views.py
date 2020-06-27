from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
import json
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
            return HttpResponseRedirect('/')  # reload page - avoiding duplication
    else:
        form = ChallengeForm()
    return render(request, 'challenges/challenges.html', locals())


def ajaxIncrement(request):
    challenge = get_object_or_404(Challenge, pk=request.GET['id'])
    challenge.counter = challenge.counter + 1
    challenge.save()
    return HttpResponse(challenge.counter)


@csrf_protect  # cross-site request forgery protection
def ajaxSaveChallenge(request):
    challenge = get_object_or_404(Challenge, pk=request.POST['id'])
    if str(challenge.version) != request.POST['version']:
        return HttpResponse('2')
    challenge.name = request.POST['name']
    challenge.description = request.POST['description']
    challenge.duration = request.POST['duration']
    challenge.counter = request.POST['counter']
    challenge.save()
    return HttpResponse('0')


def ajaxDeleteChallenge(request):
    challenge = get_object_or_404(Challenge, pk=request.POST['id'])
    challenge.delete()
    return HttpResponse('0')


def ajaxGetChallenge(request):
    challenge = get_object_or_404(Challenge, pk=request.POST['id'])
    data = {'name': challenge.name, 'duration': challenge.duration,
            'counter': challenge.counter, 'version': challenge.version,
            'description': challenge.description}
    return HttpResponse(json.dumps(data))
