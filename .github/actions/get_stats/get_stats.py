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
    return pd.DataFrame(stats_dict)


def create_stats_comment(project_stats):
    payload_fname = os.getenv('GITHUB_EVENT_PATH')
    print(f"payload_fname: {payload_fname}")
    with open(payload_fname, 'r') as f:
        payload = json.load(f)
    print(f"Payload: {payload}")
    owner, repo = payload.repository.full_name.split("/")
    gh = login(token=os.getenv("secrets.GITHUB_TOKEN"))
    issue = gh.issue(owner, repo, payload.issue.number)
    issue.create_comment(project_stats)


if __name__ == "__main__":
    stats = get_project_stats()  # Need to add project name as env or secret
    create_stats_comment(stats)