from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from license_manager_simulator.models import License, LicenseInUse
from license_manager_simulator.schemas import LicenseCreate, LicenseInUseCreate, LicenseInUseRow, LicenseRow


class LicenseNotFound(Exception):
    """The requested license is not found."""


class NotEnoughLicenses(Exception):
    """The number of requested licenses is bigger than the available."""


def get_licenses(session: Session) -> list[LicenseRow]:
    db_licenses = session.execute(select(License)).scalars().all()
    return [LicenseRow.from_orm(license) for license in db_licenses]


def get_licenses_in_use(session: Session) -> list[LicenseInUseRow]:
    db_licenses_in_use = session.execute(select(LicenseInUse)).scalars().all()
    return [LicenseInUseRow.from_orm(license) for license in db_licenses_in_use]


def get_licenses_in_use_from_name(session: Session, license_name: str) -> list[LicenseInUse]:
    db_licenses_in_use = (
        session.execute(select(LicenseInUse).where(LicenseInUse.license_name == license_name)).scalars().all()
    )
    return [LicenseInUseRow.from_orm(license) for license in db_licenses_in_use]


def create_license(session: Session, license: LicenseCreate) -> LicenseRow:
    db_license = License(**license.dict())
    session.add(db_license)
    session.commit()
    session.refresh(db_license)
    return LicenseRow.from_orm(db_license)


def _is_license_available(session: Session, license_name: str, quantity: int) -> bool:
    license = session.execute(select(License).where(License.name == license_name)).scalars().first()
    return license is not None and quantity <= (license.total - license.in_use)


def create_license_in_use(session: Session, license_in_use: LicenseInUseCreate) -> LicenseInUseRow:
    if not _is_license_available(session, license_in_use.license_name, license_in_use.quantity):
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
    return LicenseInUseRow.from_orm(db_license_in_use)


def _get_licenses_in_database(
    session: Session,
    lead_host: str,
    user_name: str,
    quantity: int,
    license_name: str,
) -> list[LicenseInUse]:
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
    return licenses


def delete_license_in_use(
    session: Session,
    lead_host: str,
    user_name: str,
    quantity: int,
    license_name: str,
) -> list:
    licenses = _get_licenses_in_database(session, lead_host, user_name, quantity, license_name)
    if not licenses:
        raise LicenseNotFound()

    ids_to_delete = [license.id for license in licenses]
    for id in ids_to_delete:
        session.execute(delete(LicenseInUse).where(LicenseInUse.id == id))

    return ids_to_delete
