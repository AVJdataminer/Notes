# Maintaining GitHub stats for more than 14 days

[Towards Data Science](https://towardsdatascience.com/maintaining-github-stats-for-more-than-14-days-31653bd1d7e1)  · by  Responses

## Python code for maintaining the Github clones and views statistics for more than 14 days.

[![](https://miro.medium.com/fit/c/96/96/2*plHDluoT2sBWOnx8mgqREw.jpeg)](https://towardsdatascience.com/@aqeel.anwar?source=post_page-----31653bd1d7e1----------------------)

[Aqeel Anwar](https://towardsdatascience.com/@aqeel.anwar?source=post_page-----31653bd1d7e1----------------------)

[Jun 10](https://towardsdatascience.com/maintaining-github-stats-for-more-than-14-days-31653bd1d7e1?source=post_page-----31653bd1d7e1----------------------)  · 4 min read

GitHub is a great platform for helping developers to store and manage their code. Currently, GitHub only provides statistics for the last 14 days. These statistics include the number of views, unique views, clones, and unique clones. As a developer, I find it a little unresting not to be able to see the lifelong statistics of my GitHub repositories. These lifelong stats will help developers know the importance of their repositories. Based on the traffic, developers can give more attention to certain repositories. Also, sometimes developers might want to display these stats on their website.

In this article, I will go through in detail how to maintain GitHub statistics of your repositories for more than 14 days and display these graphs of your website. The complete code can be found  [here](https://github.com/aqeelanwar/StatTheGit).

# StatTheGit

StatTheGit is a python based tool to fetch, maintain, and display GitHub clone and views statistics. This repository can be used to maintain a local copy of the repository statistics.

## Step 1 — Clone the repository

git clone [https://github.com/aqeelanwar/StatTheGit.git](https://github.com/aqeelanwar/StatTheGit.git)

## Step 2 — Install the required packages

cd StatTheGit  
pip install -r requirements.txt

## Step 3 — Fetch the stats

python fetch_stats.py \  
--GitToken <GitToken> \  
--username <GitHub Username> \  
--RepoNames <Repository name>

![Image for post](https://miro.medium.com/max/60/1*me-EiUH1fFQa0NkKwk2s3A.png?q=20)

![Image for post](https://miro.medium.com/max/1892/1*me-EiUH1fFQa0NkKwk2s3A.png)

Arguments detail for python file fetch_the_stats.py

**GitToken:** GitToken is a 40 character hexadecimal Git Access Token that is used in place of a password to carry out git operations. To fetch the stats from your GitHub account, you will need to create a Git Access Token. Details on how to create one from your profile can be found  [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)  on the GitHub website.

**username:**  This is your GitHub username.

**RepoNames:**  can be used to limit the repositories for which you want to fetch the statistics. To fetch the statistics of more than one repositories, just separate them with space as shown in the example below

python fetch_stats.py \  
--username <username> \  
--GitToken <GitToken-here> \  
--RepoNames reponame1 reponame2 reponame3

Running fetch_stats.py will create a folder repo_stats/<username> in the parent directory. The view and clone stats for the mentioned repositories will be fetched from the GitHub profile and saved as a .txt file. If the .txt file for the repository already exists the code appends the fetched data to existing stats taking care of issues such as duplicate stats, missing dates, etc. Running fetch_stats at least once every 2 weeks will ensure that the statistics from GitHub are fetched (before they are discarded) and appended to current statistics.

# Generic  
|-- repo_stats  
|    |-- <username>  
|    |    |-- <repository 1>.txt  
|    |    |-- <repository 2>.txt  
|    |    |-- <repository 3>.txt# Example  
|-- repo_stats  
|    |-- aqeelanwar  
|    |    |-- PEDRA.txt  
|    |    |-- SocialDistancingAI.txt

![Image for post](https://miro.medium.com/max/60/1*pZTGX8EuxiWhX2Rczy56Fw.png?q=20)

![Image for post](https://miro.medium.com/max/1268/1*pZTGX8EuxiWhX2Rczy56Fw.png)

Example text file of repository statistics — SocialDistancingAI.txt

## Step 4 — Display the Stats

StatTheGit can be used to create and update both offline graphs, and online graphs of your GitHub repositories which can then be displayed on your website  [like this](http://www.aqeel-anwar.com/#GitHubStat). Plotly is used as the graphing library primarily because it supports online graphs that can be embedded into your website.

**Offline Graphs:** Plotly based interactive graphs that can be viewed on your local machine.

python display_stats.py \  
--stat_folder repo_stats \  
--display_type 'offline'

This will open up a browser tab for each repository under consideration and display an interactive graph of the repository clone and views statistics

![Image for post](https://miro.medium.com/freeze/max/60/1*uQNPsEtbTXkzYKBKOkU1mQ.gif?q=20)

![Image for post](https://miro.medium.com/max/800/1*uQNPsEtbTXkzYKBKOkU1mQ.gif)

**Online Graphs:**  To display these graphs on your website, you need to host them at your Plotly account. Following steps can be taken

1.  Create Plotly account  [here](https://chart-studio.plotly.com/feed/#/)  (_plotly-username_)
2.  Generate API Key  [here](https://plot.ly/settings/api)  (_plotly-api_key_)

Once you have the username and the API key you can use the following command to create online graphs that can then be shared on websites.

python display_stats.py \  
--stat_folder repo_stats \  
--display_type 'online' \  
--username <plotly-username> \  
--api_key <plotly-api-key

Running this command will open up the graphs for each considered repository in the web browser. To display these graphs on your website, you can copy the iframe or HTML code (based on your website design) and use it on your website.

![Image for post](https://miro.medium.com/freeze/max/60/1*JU708gFZd6gQFu0odVGTBQ.gif?q=20)

![Image for post](https://miro.medium.com/max/800/1*JU708gFZd6gQFu0odVGTBQ.gif)

The link will not change when you run the command again and the graphs displayed on your websites will automatically get updated hence omitting the need of copy-pasting the link again.

## Step 5 — Update the Stats:

Now from this point onwards whenever you need to update the GitHub statistics displayed on your website, you only need to run fetch_stats and display_stats

**# Step 1:**python fetch_stats.py \  
--GitToken <GitToken> \  
--username <GitHub Username> \  
--RepoNames <Repository name>**#Step 2:**python display_stats.py \  
--stat_folder repo_stats \  
--display_type 'online' \  
--username <plotly-username> \  
--api_key <plotly-api-key

This will automatically update the graphs.

# Summary:

[StatTheGit](https://github.com/aqeelanwar/StatTheGit)  can be used to maintain and automatically update the  **life-long** statistics of your GitHub repositories on your website.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjMyMjM0NTQ5LC04ODk3NTE3NzVdfQ==
-->