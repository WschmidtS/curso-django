from django.shortcuts import render

videos = [
    {'slug': '6demoday', 'titulo': '6º Demo Day - Polo Digital de Mogi das Cruzes', 'vimeo_id': 439637023},
    {'slug': 'apresentacao_sebrae', 'titulo': 'Apresentação TecAcademy - Tarefa Sebrae', 'vimeo_id': 439733389},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(resquest):
    return render(resquest, 'demoday/indice.html', context={'videos': videos})


def video(resquest, slug):
    video = videos_dct[slug]
    return render(resquest, 'demoday/video.html', context={'video': video})
