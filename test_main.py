from main import app
from fastapi.testclient import TestClient
from mylib.logic import wiki, phrase

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia api"}


def test_read_search():
    response = client.get("/search/Uzbekistan")
    assert response.status_code == 200
    assert response.json() == {
        "result": "Uzbekistan (Uzbek: Oʻzbekiston, Ўзбекистон; UK: , US:  ), officially the Republic of Uzbekistan (Oʻzbekiston Respublikasi, Ўзбекистон Республикаси), is a country located in Central Asia."
    }


@app.get("/phrases/{name}")
def test_read_phrases():
    response = client.get("/phrases/Uzbekistan")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "uzbekistan",
            "uzbek",
            "oʻzbekiston",
            "uk",
            "uzbekistan",
            "oʻzbekiston respublikasi",
            "ўзбекистон республикаси",
            "asia",
        ]
    }
