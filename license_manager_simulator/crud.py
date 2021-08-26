from pydantic.tools import parse_obj_as
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from license_manager_simulator.models import License, LicenseInUse
from license_manager_simulator.schemas import LicenseRow, LicenseCreate, LicenseInUseRow, LicenseInUseCreate


class LicenseNotFound(Exception):
    """The requested license is not found."""


class NotEnoughLicenses(Exception):
    """The number of requeted licenses if bigger than the available."""


def get_licenses(session: Session) -> list[LicenseRow]:
    return session.execute(select(License)).scalars().all()


def get_licenses_in_use(session: Session) -> list[LicenseInUseRow]:
    return session.execute(select(LicenseInUse)).scalars().all()


def get_licenses_in_use_from_id(session: Session, license_name: str) -> list[LicenseInUse]:
    return session.execute(select(LicenseInUse).where(LicenseInUse.license_name == license_name)).scalars().all()


def create_license(session: Session, license: LicenseCreate) -> LicenseRow:
    db_license = License(**license.dict())
    session.add(db_license)
    session.commit()
    session.refresh(db_license)
    return db_license


def create_license_in_use(session: Session, license_in_use: LicenseInUseCreate) -> LicenseInUseRow:
    license = session.execute(select(License).where(License.name == license_in_use.license_name)).scalars().first()
    if license_in_use.quantity > (license.total - license.in_use):
        raise NotEnoughLicenses()

    session.execute(
        update(License)
        .where(License.name == license_in_use.license_name)
        .values(in_use=license_in_use.quantity)
    )
    db_license_in_use = LicenseInUse(**license_in_use.dict())
    session.add(db_license_in_use)
    session.commit()
    session.refresh(db_license_in_use)
    return db_license_in_use


def delete_license_in_use(session: Session, lead_host: str, user_name: str, quantity: int, license_name: str) -> list:
    stmt = (
        select(LicenseInUse)
        .join(License)
        .where(
            License.name == license_name,
            LicenseInUse.lead_host == lead_host,
            LicenseInUse.user_name == user_name,
            LicenseInUse.quantity == quantity,
        )
    )
    licenses = session.execute(stmt).scalars().all()
    if not licenses:
        raise LicenseNotFound()

    ids_to_delete = [license.id for license in licenses]
    for id in ids_to_delete:
        session.execute(delete(LicenseInUse).where(id=id))

    return ids_to_delete
