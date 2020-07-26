from django.shortcuts import render, get_object_or_404

from pypro.demoday.models import Video


def indice(resquest):
    videos = Video.objects.order_by('creation').all()
    return render(resquest, 'demoday/indice.html', context={'videos': videos})


def video(resquest, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(resquest, 'demoday/video.html', context={'video': video})
