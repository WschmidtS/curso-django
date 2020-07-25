import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('demoday:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        '6º Demo Day - Polo Digital de Mogi das Cruzes',
        'Apresentação TecAcademy - Tarefa Sebrae'
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)

@pytest.mark.parametrize(
    'slug',
    [
        '6demoday',
        'apresentacao_sebrae'
    ]
)
def test_link_video(resp, slug):
    video_link = reverse('demoday:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')
