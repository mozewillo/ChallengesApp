from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
import json
# Create your views here.
from challenges.models import Challenge, Category, Tag
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


def showCategories(request):
    categories = Category.objects.annotate(num_challenges=Count('challenge'))
    return render(request, 'challenges/categories.html', locals())


def showChallengesInCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    challenges = Challenge.objects.filter(category=category)
    return render(request, 'challenges/challenges_in_category.html', locals())

def showChallenge(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    return render(request, 'challenges/challenge.html', locals())

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
