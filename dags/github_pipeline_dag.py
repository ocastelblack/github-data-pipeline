from datetime import datetime

from airflow import DAG

from airflow.operators.bash import BashOperator


default_args = {
    "owner": "oscar",
    "start_date": datetime(2026, 5, 1)
}


with DAG(
    dag_id="github_data_pipeline",
    default_args=default_args,
    schedule="@daily",
    catchup=False
) as dag:

    run_pipeline = BashOperator(
        task_id="run_github_pipeline",

        bash_command="""
        cd /opt/airflow &&
        python /app/main.py
        """
    )

    run_pipeline