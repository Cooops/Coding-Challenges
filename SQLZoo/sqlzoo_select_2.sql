-- SQL ZOO practice questions @ 11/25/2018
-- https://sqlzoo.net/wiki/SELECT_from_Nobel_Tutorial

"""
Winners from 1950
1.
Change the query shown so that it displays Nobel prizes for 1950.
"""
SELECT yr, subject, winner
FROM nobel
WHERE yr = 1950;

"""
1962 Literature
2.
Show who won the 1962 prize for Literature.
"""
SELECT winner
FROM nobel
WHERE yr = 1962
AND subject = 'Literature';

"""
Albert Einstein
3.
Show the year and subject that won 'Albert Einstein' his prize.
"""
SELECT yr, subject
FROM nobel
WHERE winner  = 'Albert Einstein';

"""
Recent Peace Prizes
4.
Give the name of the 'Peace' winners since the year 2000, including 2000.
"""
SELECT winner
FROM nobel
WHERE subject = 'Peace'
AND yr >= 2000;

"""
Literature in the 1980's
5.
Show all details (yr, subject, winner) of the Literature prize winners for 1980 to 1989 inclusive.
"""
SELECT *
FROM nobel
WHERE yr BETWEEN 1980 AND 1989
AND subject = 'Literature';

"""
Only Presidents
6.
Show all details of the presidential winners:

- Theodore Roosevelt
- Woodrow Wilson
- Jimmy Carter
- Barack Obama
"""
SELECT * FROM nobel
WHERE winner IN ('Theodore Roosevelt', 'Woodrow Wilson', 'Jimmy Carter', 'Barack Obama');

"""
John
7.
Show the winners with first name John
"""
SELECT winner
FROM nobel
WHERE winner LIKE ('John %');

"""
Chemistry and Physics from different years
8.
Show the year, subject, and name of Physics winners for 1980 together with the Chemistry winners for 1984.
"""
SELECT *
FROM nobel
WHERE subject = 'Physics' AND yr = '1980'
OR subject = 'Chemistry' AND yr = '1984';

"""
Exclude Chemists and Medics
9.
Show the year, subject, and name of winners for 1980 excluding Chemistry and Medicine
"""
SELECT *
FROM nobel
WHERE yr = '1980' AND subject NOT IN ('Chemistry', 'Medicine');

"""
Early Medicine, Late Literature
10.
Show year, subject, and name of people who won a 'Medicine' prize in an early year (before 1910, not including 1910) together with winners of a 'Literature' prize in a later year (after 2004, including 2004)
"""
SELECT *
FROM nobel
WHERE subject = 'Medicine' AND yr < 1910
OR subject = 'Literature' AND yr >= 2004;

"""
Harder Questions (lol)
Umlaut
11.
Find all details of the prize won by PETER GRÜNBERG
"""
SELECT *
FROM nobel
WHERE winner = 'PETER GRÜNBERG';

"""
Apostrophe
12.
Find all details of the prize won by EUGENE O'NEILL
"""
SELECT *
FROM nobel
WHERE winner = "EUGENE O\'NEILL"; -- the sql file doesn't like the escaping, so using "" instead of '' (which won't work in your query)

"""
Knights of the realm
13.
Knights in order

List the winners, year and subject where the winner starts with Sir. Show the the most recent first, then by name order.
"""
SELECT winner, yr, subject
FROM nobel
WHERE winner LIKE ('Sir %')
ORDER BY yr DESC;

"""
The expression subject IN ('Chemistry','Physics') can be used as a value - it will be 0 or 1.

Show the 1984 winners and subject ordered by subject and winner name; but list Chemistry and Physics last.
"""
SELECT winner, subject
FROM nobel
WHERE yr=1984
ORDER BY subject IN ('Physics', 'Chemistry'), subject, winner;
