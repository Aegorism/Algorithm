import os
from datetime import datetime
import logging
import requests
import github
from github import Github

logging.basicConfig(
    format='[%(asctime)s] {%(filename)s} %(levelname)s - %(message)s',
    datefmt='%y-%m-%d %H:%M:%S'
)


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
    table = response.json()['results']
    return table


def get_table_contents(table: dict) -> dict:
    """
    "문제 이름", "링크" 필드의 값을 읽어오는 함수

    :param table: 노션 테이블의 모든 정보가 담긴 딕셔너리
    :return: 노션 테이블의 원하는 정보만(문제이름, 링크, 날짜) 담긴 딕셔너리
    """

    contents = {}
    for row in table:
        name = row['properties']['문제 이름']['title'][0]['plain_text']
        url = row['properties']['링크']['url']
        month = row['properties']['Month']['multi_select']
        # Month 필드가 채워진 경우
        if month:
            res = []
            for m in month:
                m = m['name'].split(" ")[1]
                m = f"{datetime.strptime(m, '%b').month:02}{m}"
                res.append(m)
            month = res
            contents.update({name: {'url': url, 'month': month}})
        # Month 필드가 채워지지 않은 경우
        else:
            logging.warning(f"<{name}>의 Month 필드가 비어 있어서 디렉토리가 생성되지 않았습니다.")

    return contents


def get_github_repo(access_token: str, organization: str, repository: str):
    """
    github repo object를 얻는 함수

    :param access_token: Github access token
    :param repository_name: repo 이름
    :return: repo object
    [코드 출처] https://github.com/zzsza/github-action-with-python/blob/22f3a6118ebc020e0869487a30f7627f69ff6bb2/github_utils.py#L4
    """

    g = Github(access_token)
    org = g.get_organization(organization)
    repo = org.get_repo(repository)
    return repo


def create_ps_dir(repo, contents, branch='main'):
    """
    레포지토리에 문제별로 디렉토리와 README.md 만드는 함수

    :param repo: repo object
    :param contents: 노션 테이블의 정보가 들어있는 딕셔너리
    :param branch: 브랜치 이름
    :return:
    """

    for problem_name, value in contents.items():
        for month in value['month']:
            is_repo = False
            try:
                if repo.get_contents(f"Problems/{month}/{problem_name}", ref=branch):
                    is_repo = True
            except github.GithubException:
                pass
            if not is_repo:
                repo.create_file(
                    path=f"Problems/{month}/{problem_name}/README.md",
                    message=f":memo: {problem_name} 문제 추가",
                    content=f"# {problem_name}\n{value['url']}",
                    branch=branch
                )


if __name__ == '__main__':
    notion_key = os.environ['NOTION_KEY']
    database_id = os.environ['DATABASE_ID']
    access_token = os.environ['ACCESS_TOKEN']
    organization = 'Aegorism'
    repository = 'Algorithm'

    table = get_notion_table(notion_key, database_id)
    contents = get_table_contents(table)
    repo = get_github_repo(access_token, organization, repository)
    create_ps_dir(repo, contents, branch='main')
