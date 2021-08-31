from fastapi import Body, Depends, FastAPI, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from license_manager_simulator import crud, models, schemas
from license_manager_simulator.database import engine, session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.post(
    "/licenses/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.LicenseRow,
)
def create_license(license: schemas.LicenseCreate, db: Session = Depends(get_db)):
    try:
        created_license = crud.create_license(db, license)
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"License already exists\n{e}")
    return created_license


@app.get(
    "/licenses/",
    status_code=status.HTTP_200_OK,
    response_model=list[schemas.LicenseRow],
)
def list_licenses(db: Session = Depends(get_db)):
    return crud.get_licenses(db)


@app.post(
    "/licenses-in-use/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.LicenseInUseRow,
)
def create_license_in_use(license_in_use: schemas.LicenseInUseCreate, db: Session = Depends(get_db)):
    try:
        created_license_in_use = crud.create_license_in_use(db, license_in_use)
    except crud.NotEnoughLicenses:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough licenses available.")
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"LicenseInUse already exists\n{e}")
    return created_license_in_use


@app.get(
    "/licenses-in-use/",
    status_code=status.HTTP_200_OK,
    response_model=list[schemas.LicenseInUseRow],
)
def list_licenses_in_use(db: Session = Depends(get_db)):
    return crud.get_licenses_in_use(db)


@app.get(
    "/licenses-in-use/{license_name}",
    status_code=status.HTTP_200_OK,
    response_model=list[schemas.LicenseInUseRow],
)
def list_licenses_in_use_from_name(license_name: str, db: Session = Depends(get_db)):
    return crud.get_licenses_in_use_from_name(db, license_name)


@app.delete(
    "/licenses-in-use/",
    status_code=status.HTTP_200_OK,
    response_model=list[int],
)
def delete_license_in_use(
    lead_host: str = Body(...),
    user_name: str = Body(...),
    quantity: int = Body(...),
    license_name: str = Body(...),
    db: Session = Depends(get_db),
):
    try:
        return crud.delete_license_in_use(db, lead_host, user_name, quantity, license_name)
    except crud.LicenseNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="License not found.")
