from django.shortcuts import render

from pypro.demoday.models import Video

videos = [
    Video(slug='6demoday', titulo='6º Demo Day - Polo Digital de Mogi das Cruzes', vimeo_id='439637023'),
    Video(slug='apresentacao_sebrae', titulo='Apresentação TecAcademy - Tarefa Sebrae', vimeo_id='439733389'),
]

videos_dct = {v.slug: v for v in videos}


def indice(resquest):
    return render(resquest, 'demoday/indice.html', context={'videos': videos})


def video(resquest, slug):
    video = videos_dct[slug]
    return render(resquest, 'demoday/video.html', context={'video': video})
