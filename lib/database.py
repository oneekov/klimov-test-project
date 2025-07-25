from sqlalchemy.schema import CreateSchema
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.models import *

class Database:
    def __init__(self, host, port, user, password, dbname):
        self.connection_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

        self.engine = create_engine(url=self.connection_url)
        self.session = sessionmaker(self.engine, expire_on_commit=False)
