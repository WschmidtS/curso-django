from django.shortcuts import render


def video(resquest, slug):
    videos = {
        '6demoday': {'titulo': '6º Demo Day - Polo Digital de Mogi das Cruzes', 'vimeo_id': 439637023},
        'apresentacao_sebrae': {'titulo': 'Apresentação TecAcademy - Tarefa Sebrae', 'vimeo_id': 0000},
    }
    video = videos[slug]
    return render(resquest, 'demoday/video.html', context={'video': video})
