from kifur.kifu_repository.models import Kifu
from kifur.kifu_repository.models import Player
from kifur.kifu_repository.models import Tag
from django.contrib import admin

class KifuAdmin(admin.ModelAdmin):
    fieldsets = [
        ('SGF metadata', {'fields': ['sgf', 'player_white', 'player_black', 'board_size', 'handicap', 'komi', 'rules', 'event', 'date_recorded']}),
        ('Kifur metadata', {'fields': ['description', 'tags', 'visibility', 'date_published']}),
    ]
    list_display = ('player_white', 'player_black', 'board_size', 'date_recorded', 'handicap')
    
admin.site.register(Kifu, KifuAdmin)
admin.site.register(Player)
admin.site.register(Tag)