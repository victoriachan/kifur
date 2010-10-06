from kifur.kifu_repository.models import Kifu
from kifur.kifu_repository.models import Player
from kifur.kifu_repository.models import Tag
from django.contrib import admin

class KifuAdmin(admin.ModelAdmin):
    fieldsets = [
        ('SGF metadata', {'fields': ['sgf', 'player_white', 'player_black', 'board_size', 'handicap', 'komi', 'rules', 'result', 'event', 'date_recorded']}),
        ('Kifur metadata', {'fields': ['description', 'tags', 'visibility']}),
    ]
    list_display = ('label', 'player_white', 'player_black', 'result', 'board_size', 'handicap', 'date_recorded')
    list_filter = ['date_recorded', 'handicap', 'board_size']
    search_fields = ['description', 'event', 'tags__label', 'player_white__full_name', 'player_black__full_name']
    date_hierachy = 'date_recorded'
    ordering = ('-date_recorded',)

admin.site.register(Kifu, KifuAdmin)
admin.site.register(Player)
admin.site.register(Tag)