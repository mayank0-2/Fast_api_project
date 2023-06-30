from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import sessionmaker


db_url = "mysql+mysqlconnector://root:@localhost/EcomFastApi"

engine = create_engine(
    db_url
)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()