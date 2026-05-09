from sqlalchemy.orm import sessionmaker

from db import engine

from models import (
    Repository,
    Issue,
    Commit
)

Session = sessionmaker(bind=engine)


def save_repository(repo_name):

    session = Session()

    repository = (
        session.query(Repository)
        .filter_by(full_name=repo_name)
        .first()
    )

    if not repository:

        repository = Repository(
            full_name=repo_name
        )

        session.add(repository)

        session.commit()

    session.refresh(repository)

    session.close()

    return repository.id


def save_issues(repo_id, issues_data):

    session = Session()

    for issue in issues_data:

        existing_issue = (
            session.query(Issue)
            .filter_by(id=issue["id"])
            .first()
        )

        if existing_issue:
            continue

        new_issue = Issue(
            id=issue["id"],
            repo_id=repo_id,
            title=issue.get("title"),
            state=issue.get("state"),
            created_at=issue.get("created_at"),
            updated_at=issue.get("updated_at")
        )

        session.add(new_issue)

    session.commit()

    session.close()


def save_commits(repo_id, commits_data):

    session = Session()

    for commit in commits_data:

        sha = commit["sha"]

        existing_commit = (
            session.query(Commit)
            .filter_by(sha=sha)
            .first()
        )

        if existing_commit:
            continue

        commit_info = commit.get("commit", {})

        author = commit_info.get("author", {})

        new_commit = Commit(
            sha=sha,
            repo_id=repo_id,
            author_name=author.get("name"),
            message=commit_info.get("message"),
            commit_date=author.get("date")
        )

        session.add(new_commit)

    session.commit()

    session.close()