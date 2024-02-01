from datetime import datetime
from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

default_args = {
    "retries": 1,
    "start_date": datetime(2022, 1, 1),
    "image_pull_policy": "Always",
}

with DAG(
    dag_id="simple_kubernetes_dag",
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
    tags=["example"],
    max_active_runs=1,
) as dag:
    simple_task = KubernetesPodOperator(
        task_id="simple_echo_task",
        image="airflowaksxacr.azurecr.io/example:latest",
        name="simple-airflow-task"
    )
