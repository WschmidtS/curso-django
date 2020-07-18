from django.shortcuts import render


def video(resquest, slug):
    return render(resquest, 'demoday/video.html')
