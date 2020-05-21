# raw_github_links.py
from github import Github
import os

g = Github("7f04719f796d59daa6a8a58b12b4ec92c5b076c1")
#path = 'https://github.com/AVJdataminer/Notes'

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))

#f = repo.get_file_contents(path, ref)
#raw_data = f.decoded_content
