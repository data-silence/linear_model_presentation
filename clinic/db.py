# from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import URL, create_engine

connection_string = URL.create(
    'postgresql',
    username='lethalmaks',
    password='xrpAqm06UadH',
    host='ep-sparkling-fog-87757951.eu-central-1.aws.neon.tech',
    database='pets_clinic'
)

engine = create_engine(connection_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
