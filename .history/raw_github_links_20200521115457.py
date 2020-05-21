# raw_github_links.py
from github import Github

g = Github("7f04719f796d59daa6a8a58b12b4ec92c5b076c1")
repo = g.get_repo("AVJdataminer/Note")
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)
#f = repo.get_file_contents(path, ref)
#raw_data = f.decoded_content
