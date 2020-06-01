
# 01 Jun 202
- Indirect time and costs
- in order to make it successful
- cancellation
- activities of more than 15 mins
- Website update
- which projects to include and exclude
- Ideal workweek or month
	- number of clients
	- types of clients
	- indirect energy and other people in the same compaines
	- Holly from yuppy puppy dog classes
	- 
# 30 May 2020
## Creating NB grader assignments
install main module
then install additional extension tools
jupyter nbextension enable nbgrader --py --sys-prefix

split simple confirmed cases data
```def dt_splitter(date_col, X, y, test_size):
        date_col = pd.to_datetime(date_col)
        xw_date=pd.DataFrame(X).merge(date_col,left_index=True, right_index=True)
        ad = (max(xw_date.date)- min(xw_date.date)).days*test_size
        split_date = min(xw_date.date) + timedelta(days=ad)
        X_train = xw_date.loc[xw_date['date'] <= split_date].drop(['date'], axis=1).values
        X_test = xw_date.loc[xw_date['date'] > split_date].drop(['date'], axis=1).values
        yw_date=pd.DataFrame(y).merge(date_col,left_index=True, right_index=True)
        y_train=yw_date.loc[yw_date['date'] <= split_date].drop(['date'], axis=1).values
        y_test=yw_date.loc[yw_date['date'] > split_date].drop(['date'], axis=1).values
        return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test=dt_splitter(df['date'], X_scaled, y, .80)```




# 29 May 2020
# content update
[DA intro location](https://courses.thinkful.com/dabc-python-1-v1/checkpoint/1)
[DA modules location](https://courses.thinkful.com/dabc-python-1-v1/checkpoint/11)

[DS intro location](https://courses.thinkful.com/dsbc-python-1-v1/checkpoint/1)
[DS modules location](https://courses.thinkful.com/dsbc-python-1-v1/checkpoint/11)

## To remove files from git now added to gitignore
To delete jupyter checkpoints after already in Git repo locally
`git rm -r .ipynb_checkpoints/`
```
git rm --cached `git ls-files -i --exclude-from=.gitignore`
```
Use  `git clean -xdn`  to perform a dry run and see what will be removed.  
Then use  `git clean -xdf`  to execute it.
Be aware that this command will also remove  **new files**  that are not in the staging area.

## Qualified
**[ksprojects](https://www.qualified.io/hire/challenges/5eb4860778d8f7000b71d924?q=ksp)** This is a complete example with test cases and preloaded functions.

## DS Teaching tools

[Rshiny Tool for teaching R](https://allisonhorst.shinyapps.io/missingexplorer/)

# 28 May 2020
Influx db at Influx Data No-code ML and anomaly detection webinar
![enter image description here](screenshots/Screen%20Shot%202020-05-28%20at%2010.10.12%20AM)

## For qualified
- develop a test that works properly in a challenge
- use variable assignment instead of a function
- record split screen with vs code and qualified
- upload a .py solution as an additional test
- 
# 27 May 2020
## AWS Arch example
![from Blue Orange](Blue Orange Architecture)

## Adding Html to Websites: Added to resources page on aidenvjohnson as linked url.

 1.  Add the html as uploaded file in wp content
 2.  Create URL linked title and image on resources page
 3. Still need to add that page to the menus
 4. Also need to add keywords and SEO stuff on the bottom
 5. 

## Working on Qualified
mot all projects would allloq local IDE
need an example that has working unit tests

## ks project challenge
### `ksprojects`

Write functions that implements the required behaviors and passes the test cases we've written for it. You'll need to draw on what you just learned about dataframes.

A dataframe named  `ksprojects`  has been loaded for you. Use this dataframe to answer each of the following questions in the provided function.

How many rows of data are in the DataFrame?

What are the names and data types of the columns?

Do any of the columns contain null values?

Find all successful documentary projects and sort them by the amount pledged. Print the top 10 highest pledges.

Create a new column named average_per_backer and set its value to the total amount pledged / number of backers. What happened to the rows with 0 backers? How can this be dealt with?

Create a crosstab to get a count of records for each combination of state and category.

PRELOADED CODE

```
import pandas as pd
### NOTE THIS IS NOT THE CORRECT DATA - NEED URL FROM GEORGE, CAN BE HOSTED VIA S3 OR VIA GITHUB
### 5/25: Cory gave George new CSV to upload, flip out the below for the KSPROJECTS DATA


df = pd.read_csv("https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-analytics-bootcamp/ksprojects.csv")
#df = pd.read_csv("https://raw.githubusercontent.com/nychealth/coronavirus-data/master/boro.csv")
#df = pd.read_csv("https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-analytics-bootcamp/ksprojects.csv")
```

SOLUTION SETUP

```
import pandas as pd
import preloaded

ksprojects = preloaded.df

def df_count_rows(ksprojects) -> int:
    """ Return the Count of Rows """
    pass
    
def df_names_and_types(ksprojects) -> dict:
    """ What are the names and data types of the columns? 
        Return the columns and their datatype strings as a dict, e.g.:
        {"foo": "int64", "bar": "float64", "baz": "object"}
    """
    pass

def any_nulls(ksprojects) -> int:
  """ Do any of the columns contain null values 
      Return the number of columns which contain null values
  """
  pass

def top_10_docs(ksprojects) -> object:
  """ Find all successful documentary projects and sort them by the amount pledged. 
      Print the top 10 highest pledges.
      Return them as a dataframe
  """
  pass

def no_backers(ksprojects) -> int:
  """ Create a new column named average_per_backer and set its value to the total amount pledged / number of backers
    What happened to the rows with 0 backers? 
    Return the number of rows with zero backers
  """
  pass

def records_count(ksprojects) -> int:
  """ Create a dictionary to get a count of records for each state.
      Return the dictionary in the following form: {"AL":1,"AK":2}
  """
  pass
```

WORKING SOLUTION

```
### NEED ACTUAL DATA FROM GEORGE TO PRODUCE THE REFERENCE SOLUTION ###
import pandas as pd
import preloaded

df = preloaded.df

#1 How many rows are in the dataframe?
def df_count_rows(df) -> int:
    """ Return the Row Count """
    return len(df)
    
def df_names_and_types(df) -> dict:
    """ What are the names and data types of the columns? 
        Return the columns and their datatype strings as a dict, e.g.:
        {"foo": "int64", "bar": "float64", "baz": "object"}
    """
    return {k: str(v) for k, v in dict(df.dtypes).items()}

def any_nulls(df) -> int:
  """ Do any of the columns contain null values 
      Return the number of columns which contain null values
  """
  cols = df.isna().sum()
  return sum(cols>0)

def top_10_docs(ksprojects) -> object:
  """ Find all successful documentary projects and sort them by the amount pledged. 
      Print the top 10 highest pledges.
      Return them as a dataframe
  """
  return df.loc[df['state']=='successful'].sort_values(by='pledged',ascending=False).head(10).get_value(0,0, takeable=True)

def no_backers(df) -> int:
  """ Create a new column named average_per_backer and set its value to the total amount pledged / number of backers
    What happened to the rows with 0 backers? 
    Return the number of rows with zero backers
  """
  df['average_per_backer'] = df['pledged']/df['backers']
  return df['average_per_backer'].isna().sum()
  

def records_count(df) -> int:
  """ Create a crosstab to get a count of records for each combination of state and category.
      The index of the crosstab should be the category, and the columns should be the state.
  """
  return pd.crosstab(df['category'],df['state'])
```

TESTING DETAILS

Framework:

Python unittest

Total Test Cases:

3

Python Version:

3.7

TEST CASES

```
import io
import pandas
import requests
import unittest
from solution import *
import preloaded

df = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-analytics-bootcamp/ksprojects.csv')

def solution_any_nulls(df) -> int:
  cols = df.isna().sum()
  return sum(cols>0)

def solution_top_10_docs(df) -> object:
  return df.loc[df['state']=='successful'].sort_values(by='pledged',ascending=False).head(10).get_value(0,0,takeable=True)

def solution_no_backers(df) -> int:
  df['average_per_backer'] = df['pledged']/df['backers']
  return df['average_per_backer'].isna().sum()
  
def solution_records_count(df) -> int:
  return pd.crosstab(df['category'],df['state'])

class Test(unittest.TestCase):
    def setUp(self):
        #url = 'https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-analytics-bootcamp/ksprojects.csv'
        self.data = preloaded.df
        #self.data = io.StringIO(requests.get(url).text)
        
    def count_rows(self):
         self.assertEqual(df_count_rows(self.data), 6)
        
    def test_names_and_types(self):
         #expected = {'BOROUGH_GROUP': 'object', 
         #            'COVID_CASE_COUNT': 'int64', 
         #            'COVID_CASE_RATE': 'float64'}
         expected = {k: str(v) for k, v in dict(df.dtypes).items()}
         self.assertEqual(df_names_and_types(self.data), expected)        

    def test_any_nulls(self):
         self.assertEqual(any_nulls(self.data), solution_any_nulls(df))         
          
    def test_top_10_docs(self):
         self.assertEqual(top_10_docs(self.data),solution_top_10_docs(self.data))           

#    def test_no_backers(self):
#         self.assertEqual(no_backers(df), #solution_no_backers(self.data))

#    def records_count(self.data):
#         self.assertEqual(record_count(self.data),solution_records_count(df))
```

MODIFIABLE SAMPLE TESTS

```
import io
import pandas
import requests
import unittest
from solution import *

class Test(unittest.TestCase):
    def setUp(self):
        url = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/boro.csv"
        self.data = pd.read_csv(url)
        #self.data = io.StringIO(requests.get(url).text)
        
    def test_rows(self):
        self.assertEqual(df_count_rows(self.data), 6)
        
    def test_names_and_types(self):
        expected = {'BOROUGH_GROUP': 'object', 
                    'COVID_CASE_COUNT': 'int64', 
                    'COVID_CASE_RATE': 'float64'}
        self.assertEqual(df_names_and_types(self.data), expected)

```


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
eyJoaXN0b3J5IjpbMTQ5OTc1MTQ3MiwtMjAzMDgzMzA4MCwxMz
gxNTE2ODcsMjMyODk1NTQzLDE4MTMzNzA3NDIsLTE4OTQ5Mjgz
NSwtOTIzNzU0NDk4LC04MzczOTc5ODcsMTU0MDg0ODIwOCwxMj
cyNTE0NzkwLC0xOTQyNDA4NTY2LC0xMTQ5NjcxOTcxLC01Mjc5
ODQ0NDgsMTM0NTQ5NDc4NiwxNTc1NTU2MTEyLC03MzU4MjcyMT
YsODQ1MjU2OTQxLC0xNzA2Mzg4MTI0LC00NTkwMjUxMjksMTQx
NTE2Nzc4Ml19
-->