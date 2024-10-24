from django import forms
from .models import *

# class VoteForm(forms.ModelForm):
#     class Meta:
#         model = Vote
        
class VoteForm(forms.Form):
    fantasy = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        label="Choose your favorite"
    )
    email = forms.EmailField(required=False, label="Seu Email", widget=forms.EmailInput(attrs={"placeholder": "seu@email.com", "class":"form-control"}))
    
    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields["fantasy"].choices = [(fantasy.pk, fantasy.name) for fantasy in Fantasy.objects.all()]