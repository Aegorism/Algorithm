import os
import requests
import github
from github import Github


def get_notion_table(notion_key: str, database_id: str) -> dict:
    """
    노션에 있는 표(table)에서 내용 읽어오는 함수
    :param notion_key: 노션 API key
    :param database_id: 노션 표 주소값
    :return: 노션 표 정보가 담긴 딕셔너리
    """

    base_url = "https://api.notion.com/v1/databases/"
    header = {"Authorization": notion_key, "Notion-Version": '2021-08-16'}
    response = requests.post(base_url + database_id + "/query", headers=header)
    contents = response.json()['results']
    return contents


def get_name_url(contents: dict) -> dict:
    """
    "문제 이름", "링크" 필드의 값을 읽어오는 함수
    :param contents: 노션 표 정보가 담긴 딕셔너리
    :return: 문제이름(key) - 링크(value)로 구성된 딕셔너리
    """

    problems = {}
    for content in contents:
        name = content['properties']['문제 이름']['title'][0]['plain_text']
        url = content['properties']['링크']['url']
        problems.update({name: url})

    return problems


def get_github_repo(access_token: str, repository_name: str):
    """
    https://github.com/zzsza/github-action-with-python/blob/22f3a6118ebc020e0869487a30f7627f69ff6bb2/github_utils.py#L4
    github repo object를 얻는 함수
    :param access_token: Github access token
    :param repository_name: repo 이름
    :return: repo object
    """

    g = Github(access_token)
    repo = g.get_user().get_repo(repository_name)
    return repo


def create_problem_dir(repo, problems):
    """
    레포지토리에 문제별로 디렉토리와 README.md 만드는 함수
    :param repo: repo object
    :param problems: 문제이름(key) - 링크(value)로 구성된 딕셔너리
    """

    for name, url in problems.items():
        try:
            repo.create_file(
                path=f"{name}/README.md",
                message=f":memo: {name} 문제 추가",
                content=f"# {name}\n{url}",
                branch='main'
            )
        except github.GithubException:
            pass


def delete_problem_dir(repo, problems):
    """
    레포지토리에 있는 디렉토리 지우는 함수
    :param repo: repo object
    :param problems: 문제이름(key) - 링크(value)로 구성된 딕셔너리
    """

    for name in problems:
        repo.delete_file(
            path=f"{name}/README.md",
            message=f":fire: {name} 문제 삭제",
            sha=repo.get_contents(name)[0].sha,
            branch='main'
        )


if __name__ == '__main__':
    notion_key = os.environ['NOTION_KEY']
    database_id = os.environ['DATABASE_ID']
    access_token = os.environ['ACCESS_TOKEN']
    repository_name = 'automatic-create-ps-directory'

    contents = get_notion_table(notion_key, database_id)
    problems = get_name_url(contents)
    repo = get_github_repo(access_token, repository_name)
    create_problem_dir(repo, problems)
