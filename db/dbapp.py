from sqlalchemy import Column, Integer, String, Float, Boolean

from db import Base


class DbApp(Base):
    __tablename__ = 'application'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(64))
    company_domain = Column(String(64))
    stage = Column(Integer)
    job_title = Column(String(64))
    hourly_compensation = Column(Integer)
    date_of_decision = Column(Integer)
    gender = Column(Integer)
    sexual_orientation = Column(Integer)
    racial_origin = Column(Integer)
    visa_status = Column(Integer)
    nationality = Column(Integer)
    disability = Column(Integer)
    veteran_status = Column(Integer)
    criminal_background = Column(Integer)
    indigenous = Column(Integer)
    marriage_status = Column(Integer)
    education_level = Column(Integer)
    graduated = Column(Boolean)
    years_of_experience = Column(Integer)
    co_op_term = Column(Integer)
    gpa = Column(Float)

    def __repr__(self):
        return f"Application(id={self.id!r}, name={self.company_name!r})"
