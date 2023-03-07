# controllers/default.py

def index():
    # list all tasks
    tasks = db().select(db.tasks.ALL)
    return dict(tasks=tasks)

def add_task():
    # create a new task
    task_id = db.tasks.insert(
        task_name=request.vars.task_name
    )
    redirect(URL('default', 'index'))

