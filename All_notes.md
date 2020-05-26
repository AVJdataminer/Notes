# 26 May 2020

## Notes from call with Shovon
Current places [hiring spreadsheet](https://docs.google.com/spreadsheets/d/1cVq37hFt1woa_ap8-KQFDERaXFJMYOX-Mpv5VkYkrgA/htmlview) he sent. he is going to find 3-5 jobs on this list for us to review together next call.
### For the COVID19 project
[ ] Send him a six notebook with forecasts and discussion

### For his next project
[Build a project to get hired article by Jeremie Harris.](https://towardsdatascience.com/want-to-get-hired-build-a-project-with-a-win-condition-6526d90a247d)



Email to Shama
Ideas for improving text classifier:
  - Focus on identifying the main six characters only. The two characters model performed best in your tests, building multiple two class models with the two classes including one male and one female character in each would generate better performance results and then report the results in a nice table as you did for your current classification results. I would try a Random Forest model, or something that can handle highly correlated well.
  - Some other improvements you caould add would be to generate additionals features to include in the model such as the episode, number of lines, date of the episode. These additonal features could help. 
  - Also, a potential way to create seperation among characters would be to apply a [cosine similarity algorithm](https://kite.com/python/answers/how-to-find-the-cosine-similarity-between-two-vectors-in-python) and use the scores as a feature or a cut off for classifications.
   
 - You could build a RNN and see if you can succesffuly create text
   generated from the characters lines. 


# 22 May 2020
## Qualified notes from meeting with George
Seaborn plots not displaying at all
Matplotlib plot to show 
test out the pandas.head() function
sign up for this:
[connect qualified to local IDE](https://www.qualified.io/blog/posts/developers-can-now-complete-qualified-assessments-in-their-own-ide)

## Connecting to icloud via terminal
`/Users/aidenjohnson/Library/Mobile Documents/com~apple~CloudDocs/`

## Cleaning up Ec2 to work on Thinkful content
To move local files to new github repo
`git init` - converts to a git directory
`git add .` - adds files to tracking
`git remote add origin https://github.com/username/new_repo` - adds remote
`git push -f origin master:master` - pushes files to new github repo

How to delete a git hub repo:
```
rm -rf <repo_folder>/.git
```
To view a markdown file in browser from SSH connection
install [Grip](https://github.com/joeyespo/grip)
```
pip install grip
```
```
grip -b example.md
```
A file is hosted that you can navigate to in your browser.


# 21 May 2020
- [create a keyboard shortcut for date and time on mac](https://discussions.apple.com/thread/8651300)
 - just simple git repo for now
 - Check out [Fastpages for github pages](https://fastpages.fast.ai/) blog with markdowns
 - Wrote a script called 'git_url.py' to create permanent links for images from browser url. 
 
### From AWS marketplace developer ML powered solution
 - model zoo's
 - transfer learning to adapt current models to specific needs
 - everything built has an api included
 - Plug models into applications
 
Example projects:
	
 - Mobility Explorer - real time traffic in city using object detetion and ui integration (demo on dev post website)
 - Images saved in screen shot folder on daily notes folder
 ![](https://raw.githubusercontent.com/AVJdataminer/Notes/master/screenshots/Screen%20Shot%202020-05-21%20at%2010.28.46%20AM.png)

![enter image description here](https://raw.githubusercontent.com/AVJdataminer/Notes/master/screenshots/Screen%20Shot%202020-05-21%20at%2010.30.46%20AM.png)


 - 
## How to change Screenshot folder
`defaults write com.apple.screencapture location `


## How to save and quit the vi or vim text editor

To save and quit the vi or vim editor with saving any changes you have made:

1.  If you are currently in insert or append mode, press  Esc  key.
2.  Press  :  (colon). The cursor should reappear at the lower left corner of the screen beside a colon prompt.
3.  Enter the following command (type  :x  and press  Enter  key):
    
    :x
#### 20 May 2020

 - This is tough
 - I can't decide on the best tool
 - Need to work on new checkpoints for thinkful
 - Need to work on Website on webflow

# section for todoist items

- Upload Medium articles as markdowns
--  First copy and paste to stack edit then save as markdown and html
- delete blot github rpeo
- Upload short courses to github as markdowns and html's
- Upload guided capstone notebooks as markdown and html as well as Jupyter
- Set up auto forward from amazon to todoist packages
- write a program to create raw urls for notes screenshots and all other files on github
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzOTE3MjE4NTIsMTIxMTU3MDY3OCw0OD
YzOTI4NTgsLTgzNTUzOTEyLDMwMDIzNjg2MywtNjI3ODYwMTA1
LC02NDI5MzgzNDcsLTI0NTc0OTUyNiwxMDUxMDgwNjk1LDc3ND
E2NTcwNSwtMTI4MDk3OTgzMywxOTY3MDg2MzE3LDQ5NDIwMjU5
MSwxOTM4ODU4MDc1LC0xNDkyNDk5NTk0LDk4OTE0ODk1NCwtMT
k4ODY0MzgxNSwtMTQ0NDcwNTgzLC02NDU4MjAyNDYsMjA0MzMw
NTQ4Ml19
-->