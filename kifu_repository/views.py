from django.shortcuts import render_to_response, get_object_or_404
from kifur.kifu_repository.models import Kifu
from kifur.kifu_repository.models import Player
from kifur.kifu_repository.models import Tag

def index(request):
    kifu_list = Kifu.objects.all().order_by('-date_created')[:10]
    return render_to_response('kifu_repository/index.html', {'kifu_list': kifu_list})

def kifu_index(request):
    kifu_list = Kifu.objects.all().order_by('-date_created')[:10]
    return render_to_response('kifu_repository/index.html', {'kifu_list': kifu_list})
    
def kifu_add(request):
    return HttpResponse("kifu_add")
    
def kifu_edit(request, kifu_id):
    this_kifu = get_object_or_404(Kifu, pk=kifu_id)
    return render_to_response('kifu_repository/kifu_edit.html', {'kifu': this_kifu})

def kifu_detail(request, kifu_id):
    this_kifu = get_object_or_404(Kifu, pk=kifu_id)
    return render_to_response('kifu_repository/kifu_detail.html', {'kifu': this_kifu})

def player_detail(request, player_id):
    this_player = get_object_or_404(Player, pk=player_id)
    return render_to_response('kifu_repository/player_detail.html', {'player': this_player})