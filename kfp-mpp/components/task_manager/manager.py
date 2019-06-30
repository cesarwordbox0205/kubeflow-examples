import fire
import json
from pathlib import Path


class TaskManager:

  def dispatch_tasks(self):
    tasks = {
      task_id: {
        'task-param1': 'task-'+str(task_id)+'-v1',
        'task-param2': 'task-' + str(task_id)+'-v2'
      }
      for task_id in range(10)
    }

    # Write output to file
    Path('tasks').parent.mkdir(parents=True, exist_ok=True)
    Path('tasks').write_text(json.dumps(tasks))

  def acknowledge_task(self, task_id):
    print("Task {} succeeded.".format(task_id))


def main(operation, **args):

  manager = TaskManager()

  # Dispatch tasks
  if operation == 'dispatch':
    print('Dispatching tasks')
    manager.dispatch_tasks()

  # Acknowledge task completion
  elif operation == 'acknowledge':
    if 'task_id' not in args:
      raise ValueError('task_id has to be supplied.')

    print('Acknowledge task...')
    task_id = args['task_id']
    manager.acknowledge_task(task_id)


  else:
    raise ValueError(
      'Invalid operation name: {}. Valid operations: dispatch | ack'.format(operation))


if __name__ == '__main__':
  fire.Fire(main)