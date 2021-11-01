import pytest
from django.urls import reverse


@pytest.mark.django_db()
def test_index_page(client, tour):
    index_url = reverse("index")

    response = client.get(index_url)
    content = response.content.decode("utf-8")

    assert response.status_code == 200
    assert "Для тех, кого отвлекают дома" in content
    assert tour.description in content
    assert str(tour.id) in content
