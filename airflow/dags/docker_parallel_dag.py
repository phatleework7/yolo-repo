from datetime import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
    dag_id='parallel_docker_jobs',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    job1 = DockerOperator(
        task_id='run_job1',
        image='python:3.11-slim',
        command='python -c "print(\'Job 1 done!\')"',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
    )

    job2 = DockerOperator(
        task_id='run_job2',
        image='python:3.11-slim',
        command='python -c "print(\'Job 2 done!\')"',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
    )

    job3 = DockerOperator(
        task_id='run_job3',
        image='python:3.11-slim',
        command='python -c "print(\'Job 3 done!\')"',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
    )

    [job1, job2, job3]

#new tech