from django.shortcuts import render
from feed.models import Post

# Create your views here.

def getfeed(request):
    #increment = int(request.GET.get('increment'))
    #increment_to = increment + 10
    object_list = Post.objects.all().order_by("-date")#[increment:increment_to]
    return render(request, 'feed/getfeed.html', {'object_list': object_list})