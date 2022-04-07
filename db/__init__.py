from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

engine = create_engine("sqlite+pysqlite:///db.sqlite", echo=True, future=True)
mapper_registry = registry()
Base = mapper_registry.generate_base()
Session = sessionmaker(bind=engine)

from . import dbapp

mapper_registry.metadata.create_all(engine)
