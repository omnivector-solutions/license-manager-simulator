from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from license_manager_simulator.database import Base


class License(Base):
    __tablename__ = "licenses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    total = Column(Integer)
    in_use = Column(Integer, default=0)

    licenses_in_use = relationship("LicenseInUse", back_populates="license")


class LicenseInUse(Base):
    __tablename__ = "licenses_in_use"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    user_name = Column(String)
    lead_host = Column(String)
    license_name = Column(String, ForeignKey("licenses.name"))

    license = relationship("License", back_populates="licenses_in_use")
