# Challenge Set 9
## Part III: Soccer Data

*Introductory - Intermediate level SQL*

--

Please complete this exercise using sqlite3 and Jupyter notebook.

Download the [SQLite database](https://www.kaggle.com/hugomathien/soccer/downloads/soccer.zip) and load in your notebook using the sqlite3 library. 

1. Which team scored the most points when playing at home?  

2. ```
    SELECT home_team_api_id, max(home_team_goal) as max_goals FROM Match GROUP BY home_team_api_id ORDER BY max(home_team_goal) DESC;
    ```

2. Did this team also score the most points when playing away?  No.

```
SELECT home_team_api_id, sum(away_team_goal) as sum_goals FROM Match GROUP BY home_team_api_id ORDER BY sum(away_team_goal) DESC LIMIT 1;
```

3. How many matches resulted in a tie?  6596

```
SELECT count(*) as Ties FROM Match WHERE home_team_goal = away_team_goal;
```

4. How many players have Smith for their last name? How many h	ave 'smith' anywhere in their name? 15, 18

```
SELECT count(*) as smiths FROM Player WHERE trim(substr(player_name, instr(player_name, ' '))) = 'Smith';

SELECT count(*) as smiths FROM Player WHERE player_name like '%Smith%';
```

5. What was the median tie score? Use the value determined in the previous question for the number of tie games. *Hint:* PostgreSQL does not have a median function. Instead, think about the steps required to calculate a median and use the [`WITH`](https://www.postgresql.org/docs/8.4/static/queries-with.html) command to store stepwise results as a table and then operate on these results. 1

```
WITH ties as (SELECT home_team_goal as tie_score, row_number() OVER (ORDER BY home_team_goal) as row FROM Match WHERE home_team_goal = away_team_goal ORDER BY home_team_goal),
LEN_TIES as (SELECT COUNT(*) as tie_count FROM ties),

SELECT tie_score AS MEDIAN_TIE_SCORE FROM Ties WHERE row = (SELECT (tie_count / 2) FROM LEN_TIES);
```

6. What percentage of players prefer their left or right foot? *Hint:* Calculate either the right or left foot, whichever is easier based on how you setup the problem. 75.23% Prefer the right foot.

```
SELECT cast(SUM(CASE WHEN preferred_foot = 'right' THEN 1 ELSE 0 END) as FLOAT) / count(*) * 100 AS pref_right FROM Player_Attributes
```

