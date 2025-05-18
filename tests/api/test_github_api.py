import pytest
from modules.api.clients.gihub import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'  


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    print(f"🔍 Найдено репозиториев: {r['total_count']}")
    #assert r['total_count'] >= 1
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']      


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_emojis_returns_dict(github_api):
    r = github_api.get_emojis()
    assert isinstance(r, dict)
    assert "smile" in r or "heart" in r


@pytest.mark.api
def test_get_commits_for_existing_repo(github_api):
    r = github_api.get_commits("octocat", "Hello-World")
    assert isinstance(r, list)
    assert "commit" in r[0]


@pytest.mark.api
def test_commit_has_author(github_api):
    commits = github_api.get_commits("octocat", "Hello-World")
    assert "author" in commits[0]
    assert commits[0]["author"] is not None    