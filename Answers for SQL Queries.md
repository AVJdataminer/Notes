


> Written with [StackEdit](https://stackedit.io/).
> What is the maximum salary for a non hof player

max salary for hof player

  

team differences in salary

# SQL Foundations III: Joining Data - Using subqueries, CASE, and WITH

Q1. Select the 'yearid', 'teamid', 'playerid' and 'salary' for all the players inducted into the hall of fame?

HInt: Implement a subquery where you first query the salary table and in the subquery you select the players where 'inducted' ='Y'.

A1.SELECT yearid, teamid, playerid, salary

FROM salaries

WHERE playerid IN

--

(SELECT playerid

FROM hof_inducted

WHERE inducted = 'Y');

  

Q2. Which players were inducted into the hall of fame while they were still alive?

Create a temporary table called 'newtable' which you fill with 'yearid' 'playerid', 'deathyear', and a new column called 'postmortem' indicating whether they were inducted before of after their death.

HInt: This combines many steps,if you're unsure start by creating the postmortem column and then add the CTE statement for a newtable.

A2. WITH newtable AS

(SELECT hof_inducted.playerid, yearid, deathyear,

CASE

WHEN yearid < deathyear THEN 'Alive'

ELSE 'Postmortem'

END AS postmortem

FROM "hof_inducted"

LEFT OUTER JOIN people

ON hof_inducted.playerid = people.playerid)

SELECT * FROM newtable

WHERE postmortem = 'Alive';

  

Q3.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY3MTIxMzU0Ml19
-->