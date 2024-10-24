from django import forms
from .models import *

# class VoteForm(forms.ModelForm):
#     class Meta:
#         model = Vote
        
class VoteForm(forms.Form):
    fantasy = forms.ChoiceField(
        choices=[(fantasy.pk, fantasy.name) for fantasy in Fantasy.objects.all()],
        widget=forms.RadioSelect,
        label="Choose your favorite"
    )
    email = forms.EmailField(required=False, label="Seu Email", widget=forms.EmailInput(attrs={"placeholder": "seu@email.com", "class":"form-control"}))