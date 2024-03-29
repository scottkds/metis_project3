# Challenge Set 9
## Part II: Baseball Data

*Introductory - Intermediate level SQL*

--

Please complete this exercise via SQLalchemy and Jupyter notebook.

We will be working with the Lahman baseball data we uploaded to your AWS instance in class. 


1. What was the total spent on salaries by each team, each year?


    ```
        SELECT teamid, yearid, sum(salary) as total_salary FROM salaries GROUP BY teamid, yearid ORDER BY yearid, teamid
    ```

2. What is the first and last year played for each player? *Hint:* Create a new table from 'Fielding.csv'.


~~~sql
```
    SELECT playerid, min(yearid) as First_Year, max(yearid) as Last_Year
    FROM Fielding
    GROUP BY playerid
    ```
~~~

3. Who has played the most all star games?

```
SELECT playerid, count(*) FROM AllStarFull GROUP BY playerid ORDER BY count(*) DESC LIMIT 1;
```

4. Which school has generated the most distinct players? *Hint:* Create new table from 'CollegePlaying.csv'.

```
SELECT schoolid, count(distinct(playerid)) FROM schoolsplayers GROUP BY schoolid ORDER BY count(distinct(playerid)) DESC LIMIT 20;
```

5. Which players have the longest career? Assume that the `debut` and `finalGame` columns comprise the start and end, respectively, of a player's career. *Hint:* Create a new table from 'Master.csv'. Also note that strings can be converted to dates using the [`DATE`](https://wiki.postgresql.org/wiki/Working_with_Dates_and_Times_in_PostgreSQL#WORKING_with_DATETIME.2C_DATE.2C_and_INTERVAL_VALUES) function and can then be subtracted from each other yielding their difference in days.

```
SELECT playerid, debut, finalgame, (finalgame - debut) AS LEN_CAREER FROM master WHERE debut is not null AND finalgame is not null ORDER BY (finalgame - debut) DESC LIMIT 10;
```

6. What is the distribution of debut months? *Hint:* Look at the `DATE` and [`EXTRACT`](https://www.postgresql.org/docs/current/static/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT) functions.

```
SELECT extract(month from debut), count(*) as debut_month FROM master WHERE debut is not null GROUP BY extract(month from debut) ORDER BY extract(month from debut) LIMIT 12;
```

7. What is the effect of table join order on mean salary for the players listed in the main (master) table? *Hint:* Perform two different queries, one that joins on playerID in the salary table and other that joins on the same column in the master table. You will have to use left joins for each since right joins are not currently supported with SQLalchemy.

```
SELECT salaries.playerid, avg(salary) as avg_salary FROM salaries LEFT JOIN master on salaries.playerid = master.playerid GROUP BY salaries.playerid ORDER BY salaries.playerid;

SELECT master.playerid, avg(salary) as avg_salary FROM master LEFT JOIN salaries on master.playerid = salaries.playerid GROUP BY master.playerid ORDER BY master.playerid;

Answer: Left joining salries on master results in a smaller table because the resulting table only has rows for players that have salary data in the database. Left joining master on salaries results in a much larger table because the master has many playersids that are not in the salaries database and there are many null values in the resulting table.
```

