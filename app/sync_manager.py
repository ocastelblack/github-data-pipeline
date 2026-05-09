from datetime import datetime
from sqlalchemy.orm import sessionmaker

from db import engine
from models import SyncMetadata

Session = sessionmaker(bind=engine)


def get_last_sync(repo_name, entity_type):

    session = Session()

    sync = (
        session.query(SyncMetadata)
        .filter_by(
            repo_name=repo_name,
            entity_type=entity_type
        )
        .first()
    )

    session.close()

    if sync:
        return sync.last_sync.isoformat()

    return None


def update_last_sync(repo_name, entity_type):

    session = Session()

    sync = (
        session.query(SyncMetadata)
        .filter_by(
            repo_name=repo_name,
            entity_type=entity_type
        )
        .first()
    )

    now = datetime.utcnow()

    if sync:

        sync.last_sync = now

    else:

        sync = SyncMetadata(
            repo_name=repo_name,
            entity_type=entity_type,
            last_sync=now
        )

        session.add(sync)

    session.commit()

    session.close()