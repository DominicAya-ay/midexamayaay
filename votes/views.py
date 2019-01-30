from django.shortcuts import render, redirect
from .models import Position, Vote, Candidate
from .forms import PositionModelForm, VoteModelForm, CandidateModelForm

# Create your views here.

def index(request):
    context = {}
    context['candidates'] = Candidate.objects.all().order_by('position')
    return render(request, 'index.html', context)

def candidate_create(request):
    context = {}
    context['form'] = CandidateModelForm()

    if request.method == 'POST':
        form = CandidateModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/votes/')
        else:
            return render(request, 'candidate_create.html', context)
    else:
        return render(request, 'candidate_create.html', context)

def candidate_detail(request, candidate_id):
    context = {}
    context['candidate'] = Candidate.objects.get(id=candidate_id)
    return render(request, 'candidate_detail.html', context)

def candidate_update(request, candidate_id):
    context = {}
    post = Candidate.objects.get(id=candidate_id)

    if request.method == 'POST':
        form = CandidateModelForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/votes/' + str(candidate_id))
        else:
            context['form']  = form
            return render(request, 'candidate_update.html', context)

    else:
        context['form'] = CandidateModelForm(instance=post)
    return render(request, 'candidate_update.html', context)

def position_create(request):
    context = {}
    context['form'] = PositionModelForm()

    if request.method == 'POST':
        form = PositionModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/votes/')
        else:
            return render(request, 'position_create.html', context)
    else:
        return render(request, 'position_create.html', context)

def vote(request, candidate_id):
    print("here" + str(candidate_id))
    x = Vote(candidate = Candidate.objects.get(id=candidate_id))
    x.save()
    return redirect('/votes/')
