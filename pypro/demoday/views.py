from django.shortcuts import render


def video(resquest, slug):
    video = {'titulo': '6º Demo Day - Polo Digital de Mogi das Cruzes', 'vimeo_id': 439637023}
    return render(resquest, 'demoday/video.html', context={'video': video})
