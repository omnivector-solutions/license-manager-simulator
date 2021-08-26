from sqlalchemy import select

from license_manager_simulator import crud
from license_manager_simulator.models import License, LicenseInUse


def test_create_license(one_license, session):
    created_license = crud.create_license(session, one_license)
    assert created_license.id
    assert created_license.name == one_license.name
    assert created_license.total == one_license.total
    assert len(session.execute(select(License)).scalars().all()) == 1


def test_get_licenses_empty(session):
    licenses = crud.get_licenses(session)
    assert len(licenses) == 0


def test_get_licenses(session):
    session.add(License(id=1, name="name1", total=10))
    session.add(License(id=2, name="name2", total=10))
    session.commit()

    licenses_response = crud.get_licenses(session)
    assert len(licenses_response) == 2
    assert licenses_response[0].id == 1
    assert licenses_response[0].name == "name1"
    assert licenses_response[0].total == 10
    assert licenses_response[1].id == 2
    assert licenses_response[1].name == "name2"
    assert licenses_response[1].total == 10


def test_create_license_in_use(session, one_license_in_use):
    session.add(License(id=1, name="test_name", total=10))
    session.commit()

    created_license_in_use = crud.create_license_in_use(session, one_license_in_use)
    assert created_license_in_use.id
    assert created_license_in_use.quantity == one_license_in_use.quantity
    assert created_license_in_use.user_name == one_license_in_use.user_name
    assert created_license_in_use.lead_host == one_license_in_use.lead_host
    assert created_license_in_use.license_name == one_license_in_use.license_name
    assert len(session.execute(select(LicenseInUse)).scalars().all()) == 1
