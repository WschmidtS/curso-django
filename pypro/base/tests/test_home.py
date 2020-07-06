from django.test import Client


def test_status_code(client: Client):
    resp = client.get('<html><body>Olá Django by WschmidtS</body></html>', content_type='text/html')
    assert resp.status_code == 200
