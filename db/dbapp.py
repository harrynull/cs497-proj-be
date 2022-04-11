from sqlalchemy import Column, Integer, String, Float

from db import Base


class DbApp(Base):
    __tablename__ = 'application'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(64))
    company_domain = Column(String(64))
    stage = Column(Integer)
    job_title = Column(String(64))
    gender = Column(String(32), nullable=True)
    sexual_orientation = Column(String(32), nullable=True)
    racial_origin = Column(String(32), nullable=True)
    visa_status = Column(String(32), nullable=True)
    nationality = Column(String(32), nullable=True)
    disability = Column(String(32), nullable=True)
    veteran_status = Column(String(32), nullable=True)
    criminal_background = Column(String(32), nullable=True)
    indigenous = Column(String(32), nullable=True)
    marriage_status = Column(String(32), nullable=True)
    education_level = Column(String(32), nullable=True)
    graduation_year = Column(Integer, nullable=True)
    years_of_experience = Column(Integer, nullable=True)
    gpa = Column(Float, nullable=True)

    def __repr__(self):
        return f"Application(id={self.id!r}, name={self.company_name!r})"
