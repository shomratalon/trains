"""
Get the statistics of your task's in a project

Need to define in project secrets the follow:
 - TRAINS_API_ACCESS_KEY
 - TRAINS_API_SECRET_KEY
 - TRAINS_API_HOST
 - PROJECT_NAME
 - TASK_ID
"""
import json
import os

from tabulate import tabulate
import pandas as pd
from github3 import login

from trains.backend_api.session.client import APIClient


def get_project_scalars():
    client = APIClient()
    task_id = os.getenv('TASK_ID')
    if task_id:
        task = client.tasks.get_all(id=[task_id], only_fields=["last_metrics"])
        last_metrics = task._result.response_data['tasks'][0]['last_metrics']
        data = []
        columns = []
        for metric in list(last_metrics.values()):
            for metric_vals in list(metric.values()):
                data.append(list(metric_vals.values()))
                if not columns:
                    columns = list(metric_vals.keys())
        df = pd.DataFrame(data=data, columns=columns)
        table = tabulate(df, tablefmt="github", headers="keys", showindex=False)
        return f"Task {task_id} Results\n\n{table}\n\n"
    else:
        return f"Please add `TASK_ID` to repo's secrets."


def create_stats_comment(project_stats):
    payload_fname = os.getenv('GITHUB_EVENT_PATH')
    with open(payload_fname, 'r') as f:
        payload = json.load(f)
    owner, repo = payload.get("repository", {}).get("full_name", "").split("/")
    if owner and repo:
        gh = login(token=os.getenv("GITHUB_TOKEN"))
        if gh:
            issue = gh.issue(owner, repo, payload.get("issue", {}).get("number"))
            if issue:
                issue.create_comment(project_stats)
            else:
                print(f'can not comment issue, {payload.get("issue", {}).get("number")}')
        else:
            print(f"can not log in to gh, {os.getenv('GITHUB_TOKEN')}")


if __name__ == "__main__":
    stats = get_project_scalars()
    create_stats_comment(stats)
