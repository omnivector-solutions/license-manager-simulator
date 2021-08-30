import pytest
from fastapi import status

from license_manager_simulator.models import License


def test_create_license_use(client):
    """Test that the correct status code and response are returned on in use license creation.""" 
    response = client.post(
        "/licenses/",
        json={"name": "test_name", "total": 100},
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data == {
        "id": 1,
        "name": "test_name",
        "total": 100,
        "in_use": 0,
        "licenses_in_use": [],
    }


@pytest.mark.filterwarnings("ignore::RuntimeWarning")
def test_create_license_duplicate(client, session, one_license):
    """Test that the correct response is returned when a duplicate license creation is attempted."""
    session.add(License(**one_license.dict()))
    session.commit()
    response = client.post(
        "/licenses/",
        json={"name": "test_name", "total": 100},
    )
    assert response.status_code == status.HTTP_409_CONFLICT
