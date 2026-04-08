import urllib.request


def test_home():
    response = urllib.request.urlopen("http://localhost:8080")
    assert response.status == 200

def test_health():
    response = urllib.request.urlopen("http://localhost:8080/health")
    assert response.read() == b"OK"