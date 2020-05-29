
# [Fork vs clone](https://github.community/t/the-difference-between-forking-and-cloning-a-repository/10189)

Create and checkout the new branch
`git checkout -b feature/data-wrangling`

# make code and file changes here

git add .

git commit -m 'added readme file'

git checkout master


# check changes before mergeing

git diff feature/data-wrangling

# exit by typing the letter `q`

git merge feature/data-wrangling

# show changes

git log

`q` to exit

  

Colab notebooks aren't rendering in VSC for some reason.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwOTY4OTc5NDgsLTEyMDE5ODE1OTFdfQ
==
-->