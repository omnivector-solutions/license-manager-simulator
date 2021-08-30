import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from license_manager_simulator import crud
from license_manager_simulator.models import License, LicenseInUse


def test_create_license(one_license, session):
    created_license = crud.create_license(session, one_license)
    assert created_license.id
    assert created_license.name == one_license.name
    assert created_license.total == one_license.total
    assert created_license.in_use == 0

    licenses_in_db = session.execute(select(License)).scalars().all()
    assert len(licenses_in_db) == 1
    assert licenses_in_db[0].id == created_license.id
    assert licenses_in_db[0].name == one_license.name
    assert licenses_in_db[0].total == one_license.total
    assert licenses_in_db[0].in_use == 0


# ignoring warning about double rollback
@pytest.mark.filterwarnings("ignore::RuntimeWarning")
def test_create_license_duplicate(one_license, session):
    """Test that an exception is thrown if a duplicate license entry is created."""
    crud.create_license(session, one_license)
    with pytest.raises(IntegrityError):
        crud.create_license(session, one_license)


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


def test_get_licenses_in_use(session, one_license, one_license_in_use):
    session.add(License(**one_license.dict()))
    session.add(LicenseInUse(**one_license_in_use.dict(), id=1))
    session.commit()

    licenses_in_use = crud.get_licenses_in_use(session)
    assert len(licenses_in_use) == 1
    assert licenses_in_use[0].id == 1
    assert licenses_in_use[0].quantity == one_license_in_use.quantity
    assert licenses_in_use[0].user_name == one_license_in_use.user_name
    assert licenses_in_use[0].lead_host == one_license_in_use.lead_host
    assert licenses_in_use[0].license_name == one_license_in_use.license_name


def test_get_licenses_in_use_empty(session):
    licenses_in_use = crud.get_licenses_in_use(session)
    assert len(licenses_in_use) == 0


def test_get_licenses_in_use_from_name(session, one_license, one_license_in_use):
    session.add(License(**one_license.dict()))
    session.add(LicenseInUse(**one_license_in_use.dict(), id=1))
    session.commit()

    licenses_in_use = crud.get_licenses_in_use_from_name(session, one_license.name)
    assert len(licenses_in_use) == 1
    assert licenses_in_use[0].id == 1
    assert licenses_in_use[0].quantity == one_license_in_use.quantity
    assert licenses_in_use[0].user_name == one_license_in_use.user_name
    assert licenses_in_use[0].lead_host == one_license_in_use.lead_host
    assert licenses_in_use[0].license_name == one_license_in_use.license_name


def test_get_licenses_in_use_from_name_empty(session):
    licenses_in_use = crud.get_licenses_in_use_from_name(session, "name")
    assert len(licenses_in_use) == 0


def test_create_license_in_use(session, one_license_in_use):
    session.add(License(id=1, name="test_name", total=10))
    session.commit()

    created_license_in_use = crud.create_license_in_use(session, one_license_in_use)
    assert created_license_in_use.id
    assert created_license_in_use.quantity == one_license_in_use.quantity
    assert created_license_in_use.user_name == one_license_in_use.user_name
    assert created_license_in_use.lead_host == one_license_in_use.lead_host
    assert created_license_in_use.license_name == one_license_in_use.license_name

    license_in_use_in_db = session.execute(select(LicenseInUse)).scalars().all()
    assert len(license_in_use_in_db) == 1
    assert license_in_use_in_db[0].id == created_license_in_use.id
    assert license_in_use_in_db[0].quantity == one_license_in_use.quantity
    assert license_in_use_in_db[0].user_name == one_license_in_use.user_name
    assert license_in_use_in_db[0].lead_host == one_license_in_use.lead_host
    assert license_in_use_in_db[0].license_name == one_license_in_use.license_name


@pytest.mark.filterwarnings("ignore::RuntimeWarning")
def test_create_license_in_use_duplicate(session, one_license_in_use):
    """Test that an exception is thrown if a duplicate in use license entry is created."""
    session.add(License(id=1, name="test_name", total=100))
    session.commit()

    crud.create_license_in_use(session, one_license_in_use)
    with pytest.raises(IntegrityError):
        crud.create_license_in_use(session, one_license_in_use)


def test_create_license_in_use_not_available(session, one_license_in_use):
    session.add(License(id=1, name="test_name", total=10, in_use=10))
    session.commit()

    with pytest.raises(crud.NotEnoughLicenses):
        crud.create_license_in_use(session, one_license_in_use)


def test_create_license_in_use_empty(session, one_license_in_use):
    with pytest.raises(crud.NotEnoughLicenses):
        crud.create_license_in_use(session, one_license_in_use)


def test_delete_license_in_use(session, one_license, one_license_in_use):
    session.add(License(**one_license.dict()))
    session.add(LicenseInUse(**one_license_in_use.dict(), id=1))
    session.commit()

    ids = crud.delete_license_in_use(
        session,
        one_license_in_use.lead_host,
        one_license_in_use.user_name,
        one_license_in_use.quantity,
        one_license_in_use.license_name,
    )
    assert len(ids) == 1
    license_in_use_in_db = session.execute(select(LicenseInUse)).scalars().all()
    assert len(license_in_use_in_db) == 0


def test_delete_license_in_use_not_found(session, one_license, one_license_in_use):
    session.add(License(**one_license.dict()))
    session.add(LicenseInUse(**one_license_in_use.dict(), id=1))
    session.commit()

    with pytest.raises(crud.LicenseNotFound):
        crud.delete_license_in_use(
            session,
            "wrong_lead_host",
            one_license_in_use.user_name,
            one_license_in_use.quantity,
            one_license_in_use.license_name,
        )
    license_in_use_in_db = session.execute(select(LicenseInUse)).scalars().all()
    assert len(license_in_use_in_db) == 1
