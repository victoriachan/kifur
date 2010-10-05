from django.db import models

class Tag(models.Model):
    label = models.CharField(max_length=50)
    
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
    description = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, related_name='players')
    
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
    sgf_text = models.TextField()
    player_white = models.ForeignKey(Player, related_name='player_white')
    player_black = models.ForeignKey(Player, related_name='player_black')
    board_size = models.PositiveIntegerField(default=19)
    handicap = models.PositiveIntegerField(default=0)
    komi = models.DecimalField(max_digits=5, decimal_places=1, default=6.5)
    rules = models.CharField(max_length=30, default='Japanese', choices=RULES_CHOICES)
    result = models.CharField(max_length=20)
    event = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    tags = models.ManyToManyField(Tag, related_name='kifus')
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='private')
    date_recorded = models.DateField('date recorded')
    date_published = models.DateTimeField('date published')
    date_created = models.DateTimeField('date added', auto_now_add=True)
    
    def __unicode__(self):
        return '%s vs %s : %s' % (self.player_white.full_name, self.player_black.full_name, self.result)