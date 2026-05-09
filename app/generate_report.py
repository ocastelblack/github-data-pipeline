import pandas as pd

from sqlalchemy import text

from db import engine


def generate_report():

    query = text("""

        SELECT
            r.full_name AS repository,

            COUNT(DISTINCT i.id) AS total_issues,

            COUNT(DISTINCT c.sha) AS total_commits

        FROM repositories r

        LEFT JOIN issues i
            ON r.id = i.repo_id

        LEFT JOIN commits c
            ON r.id = c.repo_id

        GROUP BY r.full_name

        ORDER BY r.full_name

    """)

    with engine.connect() as conn:

        df = pd.read_sql(query, conn)

    output_file = "github_report.csv"

    df.to_csv(output_file, index=False)

    print(f"Reporte generado: {output_file}")

    print(df)

    return output_file