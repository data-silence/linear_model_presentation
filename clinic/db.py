from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import URL, create_engine


# Реализовывал хранение данные в удаленной базе, а не словарях.
# Ничего важного в  данных нет, поэтому передаю в открытом доступе параметры подключения к базе,
# не заморачиваясь к конфигами и переменными окружения

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
