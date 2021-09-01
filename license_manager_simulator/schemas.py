from typing import List, Optional

from pydantic import BaseModel


class LicenseInUseCreate(BaseModel):
    quantity: int
    user_name: str
    lead_host: str
    license_name: str


class LicenseInUseRow(LicenseInUseCreate):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class LicenseCreate(BaseModel):
    name: str
    total: int


class LicenseRow(LicenseCreate):
    id: Optional[int] = None
    licenses_in_use: List[LicenseInUseRow] = []
    in_use: int = 0

    class Config:
        orm_mode = True
