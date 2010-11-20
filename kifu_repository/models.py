from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

class Tag(models.Model):
    label = models.CharField(max_length=100, unique=True)
    
    def __unicode__(self):
        return self.label
        
class Player(models.Model):
    RANK_CHOICES = tuple(
        [('%sk' % x, '%s kyu' % x) for x in range(30,0,-1)] +
        [('%sd' % x, '%s dan' % x) for x in range(1,9)] +
        [('%sp' % x, '%s pro' % x) for x in range(1,11)]
    )
    full_name = models.CharField(max_length=150, unique=True)
    rank = models.CharField(max_length=3, choices=RANK_CHOICES)
    description = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='players', null=True, blank=True)

    def _get_tags(self):
        return self.tags.all()
    tagged_as = property(_get_tags)
    
    def _get_games(self):
        return Kifu.objects.filter( Q(player_white=self) | Q(player_black=self))
    games = property(_get_games)

    def _get_games_count(self):
        return self.player_black.count() + self.player_white.count()
    total_games = property(_get_games_count)
    
    def __unicode__(self):
        return self.full_name

class Kifu(models.Model):
    VISIBILITY_CHOICES = (
        (u'private', u'Private'),
        (u'everyone', u'Public'),
        # (u'friends', u'Only your friends can see this'),
    )
    RULES_CHOICES = (
        (u'AGA', u'American Go Association rules'),
        (u'GOE', u'Ing rules of Goe'),
        (u'Japanese', u'Nihon-Kiin rules (Japanese)'),
        (u'NZ', u'New Zealand rules'),
    )
    sgf = models.TextField()
    player_white = models.ForeignKey(Player, related_name='player_white')
    player_black = models.ForeignKey(Player, related_name='player_black')
    board_size = models.PositiveIntegerField(default=19)
    handicap = models.PositiveIntegerField(default=0)
    komi = models.DecimalField(max_digits=5, decimal_places=1, default=6.5)
    rules = models.CharField(max_length=30, default='Japanese', choices=RULES_CHOICES)
    result = models.CharField(max_length=20, null=True, blank=True)
    event = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='kifus', null=True, blank=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='private')
    date_recorded = models.DateField('date')
    date_published = models.DateTimeField('date published')
    date_created = models.DateTimeField('date added', auto_now_add=True)
    added_by = models.ForeignKey(User, related_name='added_by', null=True)
    
    class Meta:
        verbose_name_plural = "kifu"
            
    def _get_tags(self):
        return self.tags.all()
    tagged_as = property(_get_tags)
        
    def _get_label(self):
        "Returns label for this game"
        return '%s vs %s (%s)' % (self.player_white.full_name, self.player_black.full_name, self.result)
    label = property(_get_label)

    def __unicode__(self):
        return self.label