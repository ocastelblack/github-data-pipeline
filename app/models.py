from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    TIMESTAMP,
    ForeignKey,
    BigInteger
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(255), unique=True, nullable=False)


class Issue(Base):
    __tablename__ = "issues"

    id = Column(BigInteger, primary_key=True)

    repo_id = Column(
        Integer,
        ForeignKey("repositories.id")
    )

    title = Column(Text)

    state = Column(String(50))

    created_at = Column(TIMESTAMP)

    updated_at = Column(TIMESTAMP)


class Commit(Base):
    __tablename__ = "commits"

    sha = Column(String(255), primary_key=True)

    repo_id = Column(
        Integer,
        ForeignKey("repositories.id")
    )

    author_name = Column(String(255))

    message = Column(Text)

    commit_date = Column(TIMESTAMP)


class SyncMetadata(Base):
    __tablename__ = "sync_metadata"

    repo_name = Column(String(255), primary_key=True)

    entity_type = Column(String(50), primary_key=True)

    last_sync = Column(TIMESTAMP)