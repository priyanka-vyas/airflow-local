airflow setup guide - https://towardsdatascience.com/run-airflow-docker-1b83a57616fb
create first dag in 5 min - https://marclamberti.com/blog/airflow-dag-creating-your-first-dag-in-5-minutes/

to run airflow--
docker ps
some explanation--
Catch up-The catchup parameter is set to False, which means it won't backfill or rerun any missed intervals.
dependencies of demo.py-- The dependencies between the tasks are defined using the >> operator. The training tasks (training_model_A, training_model_B, training_model_C) are set to be upstream (dependencies) of the choose_best_model task. The choose_best_model task, in turn, has two downstream tasks (accurate and inaccurate) based on the result it returns.

PythonOperator: It is a task operator that allows you to define a Python function as a task in your DAG. When the task is executed, the defined Python function is called. It is typically used for tasks that perform a specific action or computation and do not have any downstream tasks. The return value of the Python function can be passed to other tasks using xcom (cross-communication) mechanism.

BranchPythonOperator: It is a task operator that allows you to define a Python function as a branching decision point in your DAG. The Python function is called when the task is executed, and it should return the task_id of the next task to be executed based on some condition or logic. This allows you to dynamically decide which downstream tasks should be executed based on the result of the Python function. It is typically used for tasks that make decisions or control the flow of the workflow in your DAG based on some condition.


to get container id --- docker ps
docker exec -it <container id> /bin/bash ---- to go inside dags/logs/plugin
nano demo.py--- go n read the file.

