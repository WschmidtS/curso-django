from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.vimeo_id = vimeo_id
        self.titulo = titulo
        self.slug = slug

    def get_absolute_url(self):
        return reverse('demoday:video', args=(self.slug,))


videos = [
    Video('6demoday', '6º Demo Day - Polo Digital de Mogi das Cruzes', 439637023),
    Video('apresentacao_sebrae', 'Apresentação TecAcademy - Tarefa Sebrae', 439733389),
]

videos_dct = {v.slug: v for v in videos}


def indice(resquest):
    return render(resquest, 'demoday/indice.html', context={'videos': videos})


def video(resquest, slug):
    video = videos_dct[slug]
    return render(resquest, 'demoday/video.html', context={'video': video})
