import json
import os

import pandas as pd
from github3 import login

from trains.backend_api.session.client import APIClient


def get_project_stats():
    client = APIClient()
    project = client.projects.get_all(name="Tal-Proj")
    tasks = client.tasks.get_all(project=[project._result.response_data['projects'][0]['id']])
    stats_dict = {}
    for task in tasks:
        key = str(task.status)
        if key in stats_dict:
            stats_dict[key] += 1
        else:
            stats_dict[key] = 1
    return pd.DataFrame(stats_dict, columns=["Status", "Count"])


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
                issue.create_comment(project_stats.to_html())
            else:
                print(f'can not comment issue, {payload.get("issue", {}).get("number")}')
        else:
            print(f"can not log in to gh, {os.getenv('GITHUB_TOKEN')}")


if __name__ == "__main__":
    stats = get_project_stats()  # Need to add project name as env or secret
    create_stats_comment(stats)