from typing import List, Optional

from pydantic import BaseModel, root_validator


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
    in_use: Optional[int] = 0

    @root_validator()
    def in_use_validator(cls, values) -> int:
        values["in_use"] = 0
        for license_in_use in values["licenses_in_use"]:
            values["in_use"] += license_in_use.quantity
        return values

    class Config:
        orm_mode = True
