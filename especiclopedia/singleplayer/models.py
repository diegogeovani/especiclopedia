from sqlalchemy import (Column, Integer,)
from sqlalchemy.ext.declarative_base
from sqlalchemy.orm import (
        scoped_session,
        sessionmaker,
        )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class DatabaseVersion(Base):
    __tablename__ = 'SingleplayerDatabaseVersion'
    number = Column(Integer, default=1, nullable=False, unique=True)
