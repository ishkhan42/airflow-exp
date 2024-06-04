from airflow.decorators import dag, task
from airflow.models.param import Param
from datetime import datetime

def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

@task(
    task_id="calculate_nth_fibonacci"
)
def calculate_nth_fibonacci(**kwargs):
    n = kwargs['params']["index"]
    result = calculate_fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")


@dag(
    dag_id="fibonacci_dag",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["cloudav", "urls"],
    max_active_runs=1,
    params={
        "index": Param(
            description="Index of the Fibonacci number to calculate",
            default=10,
            type='integer'
        )
    },
)
def dager():
    calculate_nth_fibonacci()


d = dager()
