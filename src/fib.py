from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def calculate_nth_fibonacci(**kwargs):
    n = kwargs['dag_run'].conf.get('n')
    result = calculate_fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")

with DAG('fibonacci_dag', start_date=datetime(2022, 1, 1), schedule_interval=None) as dag:
    calculate_task = PythonOperator(
        task_id='calculate_fibonacci',
        python_callable=calculate_nth_fibonacci,
        provide_context=True
    )