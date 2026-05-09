from db import wait_for_db, create_tables

from generate_report import generate_report

from github_client import get_issues, get_commits

from insert_data import save_repository, save_issues, save_commits

from sync_manager import get_last_sync, update_last_sync

from drive_config import get_repositories

from upload_drive import upload_file

if __name__ == "__main__":

    wait_for_db()

    create_tables()

    repositories = get_repositories()

    print(f"Repositorios encontrados: {repositories}")

    for repo in repositories:

        print(f"Procesando repo: {repo}")

        repo_id = save_repository(repo)

        # ISSUES

        last_issue_sync = get_last_sync(repo, "issues")

        issues = get_issues(repo, since=last_issue_sync)

        save_issues(repo_id, issues)

        update_last_sync(repo, "issues")

        # COMMITS

        last_commit_sync = get_last_sync(repo, "commits")

        commits = get_commits(repo, since=last_commit_sync)

        save_commits(repo_id, commits)

        update_last_sync(repo, "commits")

        print(f"Issues procesados: {len(issues)}")

        print(f"Commits procesados: {len(commits)}")

    report_file = generate_report()

    try:
        upload_file(report_file)
    except Exception as e:
        print(f"Error subiendo archivo: {e}")

    print("Pipeline finalizado correctamente")
