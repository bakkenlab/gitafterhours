import requests
import dateutil.parser as dateParser


def get_commits():
    url = ""
    headers = {'Authorization': 'token '}
    request = requests.get(url, headers=headers)
    return request


def get_commits_in_range(date_from, date_to):
    commit_json = get_commits()

    commit_arr = []
    for commit in commit_json.json():
        date = commit['commit']['committer']['date']
        parsed_date = dateParser.parse(date)
        hour = parsed_date.strftime('%H')
        if int(hour) < date_from or int(hour) > date_to:
            commit_arr.append(date)

    return commit_arr

