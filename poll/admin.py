from django.contrib import admin
from .models import Fantasy, Vote

@admin.register(Fantasy)
class FantasyAdmin(admin.ModelAdmin):
    list_display = ('name', 'participant', 'image')
    search_fields = ('name', 'participant')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('fantasy', 'make', 'email')
    search_fields = ('fantasy__name', 'email')
    list_filter = ('make', 'fantasy')
