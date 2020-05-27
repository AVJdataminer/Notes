# 27 May 2020

## AWS Arch example
from Blue Orange [Screenshot]

## Adding Html to Websites: Added to resources page on aidenvjohnson as linked url.

 1.  Add the html as uploaded file in wp content
 2.  Create URL linked title and image on resources page
 3. Still need to add that page to the menus
 4. Also need to add keywords and SEO stuff on the bottom
 5. 

## Working on Qualified

[https://www.qualified.io/assess/5eb0d74d0cb708000ed49e5e/challenges/5eb0f03c0cb708000dd4a0b4](https://www.qualified.io/assess/5eb0d74d0cb708000ed49e5e/challenges/5eb0f03c0cb708000dd4a0b4)

For Python Jupyter intro
- image saved for loading error in relative path


For Modules and OOP
- need to update in text jupyter notebook to remove the modules portion.
- potentially remove the OOP for data analysts
- 
# 26 May 2020
## Call with Allyson
Need to send sign up link and jupyter notebook info.

## Call with Cihat
- In SP notes

## Notes from call with Shovon
Current places [hiring spreadsheet](https://docs.google.com/spreadsheets/d/1cVq37hFt1woa_ap8-KQFDERaXFJMYOX-Mpv5VkYkrgA/htmlview) he sent. he is going to find 3-5 jobs on this list for us to review together next call.  

[Interview Preparation document](https://docs.google.com/document/d/1m7CJsjhaiIzVpvbpLcNWqKhNXOM_9ZTxbApiJqvzq0U/edit) created by [Nabeil K.](https://www.linkedin.com/in/nabkizil/)

### For the COVID19 project
Update Github repo notebook from Copy of Colab notebook I opened today.  

Send him a six notebook with forecasts and discussion

### For his next project
- [Build a project to get hired article by Jeremie Harris.](https://towardsdatascience.com/want-to-get-hired-build-a-project-with-a-win-condition-6526d90a247d)
- Potentially build a project around getting people like him hired to North American companies for remote roles.
- Or consider Deep Racer which he feels is to many new things to learn.

## Email to Shama
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
eyJoaXN0b3J5IjpbLTE3MDYzODgxMjQsLTQ1OTAyNTEyOSwxND
E1MTY3NzgyLC05ODczNDIzNzUsLTE4MDI4NzYwMDgsLTcxMTAw
ODI3MSwxMjExNTcwNjc4LDQ4NjM5Mjg1OCwtODM1NTM5MTIsMz
AwMjM2ODYzLC02Mjc4NjAxMDUsLTY0MjkzODM0NywtMjQ1NzQ5
NTI2LDEwNTEwODA2OTUsNzc0MTY1NzA1LC0xMjgwOTc5ODMzLD
E5NjcwODYzMTcsNDk0MjAyNTkxLDE5Mzg4NTgwNzUsLTE0OTI0
OTk1OTRdfQ==
-->