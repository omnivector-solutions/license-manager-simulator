from fastapi import Depends, FastAPI, HTTPException, status
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
