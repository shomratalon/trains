import json
import os

from github3 import login

from trains import Task


def clone_and_queue():
    payload_fname = os.getenv('GITHUB_EVENT_PATH')
    with open(payload_fname, 'r') as f:
        payload = json.load(f)
    task_id, _, queue_name = payload.get("comment", {}).get("body", "").partition(" ")[2].partition(" ")  # the body should be in the form of /train-model <task_id> <queue_name>
    if task_id:
        enqueue_task = Task.get_task(task_id=task_id)
        # Clone the task to pipe to. This creates a task with status Draft whose parameters can be modified.
        gh_issue_number = payload.get("issue", {}).get("number")
        cloned_task = Task.clone(
            source_task=enqueue_task,
            name=f"{task_id} cloned task for github issue {gh_issue_number}"
        )
        Task.enqueue(cloned_task.id, queue_name=queue_name)
        owner, repo = payload.get("repository", {}).get("full_name", "").split("/")
        if owner and repo:
            gh = login(token=os.getenv("GITHUB_TOKEN"))
            if gh:
                issue = gh.issue(owner, repo, payload.get("issue", {}).get("number"))
                if issue:
                    issue.create_comment(f"New task, id:{cloned_task.id} is in queue {queue_name}")
                else:
                    print(f'can not comment issue, {payload.get("issue", {}).get("number")}')
            else:
                print(f"can not log in to gh, {os.getenv('GITHUB_TOKEN')}")


if __name__ == "__main__":
    clone_and_queue()
