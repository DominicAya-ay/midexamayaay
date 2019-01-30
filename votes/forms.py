from django.forms import ModelForm
from .models import Candidate, Position, Vote

class CandidateModelForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id']

class PositionModelForm(ModelForm):
    class Meta:
        model = Position
        exclude = ['id']

class VoteModelForm(ModelForm):
    class Meta:
        model = Vote
        exclude = ['id']
