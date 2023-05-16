from datetime import timedelta, datetime
import random
from airflow.operators.python import PythonOperator,BranchPythonOperator
from airflow import DAG
from airflow.operators.bash import BashOperator


#training model
def _training_model():
    print("in trauning modle")
    return random.randint(1,10)

#best accuracy
def _choose_best_model(ti):
    accuracies=ti.xcom_pull(task_ids=[
        'training_model_A',
        'training_model_B',
        'training_model_C'
    ])
    best_accuracy=max(accuracies)
    if (best_accuracy>8):
        return'accurate'
    return 'inaccurate'

#initiate dag objects and defining
with DAG("demo",start_date=datetime(2023,1,1),schedule="@daily",catchup=False) as dag:
    training_model_A=PythonOperator(
        task_id="training_model_A",
        python_callable=_training_model 
    )

    training_model_B=PythonOperator(
        task_id="training_model_B",
        python_callable=_training_model 
    )

    training_model_C=PythonOperator(
        task_id="training_model_C",
        python_callable=_training_model 
    )

    choose_best_model=BranchPythonOperator(
        task_id="choose_best_model",
        python_callable=_choose_best_model
    )

#accuarete or not using bash operator
    accurate=BashOperator(
        task_id="accurate",
        bash_command= "echo 'accurate'"
    )
    inaccurate=BashOperator(
        task_id="inaccurate",
        bash_command="echo 'inaccurate'"
    )
#defining dependecies
    [training_model_A,training_model_B,training_model_C]>>choose_best_model>> [accurate,inaccurate]