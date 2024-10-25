# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import Fantasy, Vote
from .forms import VoteForm
import plotly.express as px
from django.db.models import Count

def fantasy_vote_chart(request):
    # Get the count of votes for each Fantasy
    fantasias = Fantasy.objects.annotate(
        votos = Count("votes")
        ).all().order_by('-votos')
        
    fantasy_votes = (
        Vote.objects.values('fantasy__name')
        .annotate(vote_count=Count('fantasy'))
        .order_by('-vote_count')
    )
    
    # Extract the data for the graph
    names = [fv['fantasy__name'] for fv in fantasy_votes]
    counts = [fv['vote_count'] for fv in fantasy_votes]
    
    # Create a bar chart using Plotly
    fig = px.pie(
        names=names, 
        values=counts, 
        title='Votos por fantasia',
        labels={'names': 'Fantasy', 'values': 'Votes'},
        hole=0.3  # Makes it a donut chart for a more modern look
    )
    
    # Convert the Plotly figure to HTML
    graph_html = fig.to_html(full_html=False)

    # Get the top 3 Fantasy entries
    top_3 = fantasias[:3]

    context = {
        'graph_html': graph_html,
        'top_3': top_3,
    }
    
    return render(request, 'result.html', context)


def fantasy_poll(request):
    # Get all Fantasy objects to display as options
    fantasies = Fantasy.objects.all()

    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            # Create a new Vote object with the selected Fantasy
            fantasy = get_object_or_404(Fantasy, pk=form.cleaned_data['fantasy'])
            Vote.objects.create(
                fantasy=fantasy,
                make=now(),
                email=form.cleaned_data.get('email')
            )
            return redirect('thank_you')  # Redirect to a thank you page after voting
    else:
        form = VoteForm()

    context = {
        'fantasies': fantasies,
        'form': form
    }
    return render(request, 'fantasy_poll.html', context)

# views.py (add this function)
def thank_you(request):
    return render(request, 'thank_you.html')


def add_fantasy():
    pass

def view_fantasy( id=None):
    pass

