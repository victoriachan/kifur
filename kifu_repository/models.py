from django.db import models

class Tag(models.Model):
    label = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.label
        
class Player(models.Model):
    full_name = models.CharField(max_length=150, unique=True)
    rank = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    keywords = models.ManyToManyField(Tag, through='Player_Tags')
    
    def __unicode__(self):
        return self.full_name

class Kifu(models.Model):
    VISIBILITY_CHOICES = (
        (u'private', u'Only you can see this'),
        (u'everyone', u'Everyone can see this'),
        # (u'friends', u'Only your friends can see this'),
    )
    sgf_text = models.TextField()
    player_white = models.ForeignKey(Player, related_name='player_white')
    player_black = models.ForeignKey(Player, related_name='player_black')
    board_size = models.PositiveIntegerField(default=19)
    handicap = models.PositiveIntegerField(default=0)
    komi = models.DecimalField(max_digits=5, decimal_places=1, default=6.5)
    rules = models.CharField(max_length=30, default='Japanese')
    result = models.CharField(max_length=20)
    event = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    keywords = models.ManyToManyField(Tag, through='Kifu_Tags')
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='private')
    date_recorded = models.DateField('date recorded')
    date_published = models.DateTimeField('date published')
    date_created = models.DateTimeField('date added', auto_now_add=True)
    
    def __unicode__(self):
        return '%s vs %s : %s' % (self.player_white.full_name, self.player_black.full_name, self.result)
    
class Kifu_Tags(models.Model):
    tag = models.ForeignKey(Tag)
    kifu = models.ForeignKey(Kifu)
    
class Player_Tags(models.Model):
    tag = models.ForeignKey(Tag)
    player = models.ForeignKey(Player)