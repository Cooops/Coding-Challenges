-- SQL ZOO practice questions @ 11/26/2018
-- https://sqlzoo.net/wiki/SUM_and_COUNT

"""
Total world population
1.
Show the total population of the world.

world(name, continent, area, population, gdp)
"""
SELECT SUM(population)
FROM world;

"""
List of continents
2.
List all the continents - just once each.
"""
SELECT DISTINCT continent 
FROM world;

"""
GDP of Africa
3.
Give the total GDP of Africa
"""
SELECT SUM(gdp)
FROM world
WHERE continent = 'Africa';

"""
Count the big countries
4.
How many countries have an area of at least 1000000
"""
SELECT COUNT(name)
FROM world
WHERE area >= 1000000;

"""
Baltic states population
5.
What is the total population of ('Estonia', 'Latvia', 'Lithuania')
"""
SELECT SUM(population)
FROM world
WHERE name IN ('Estonia', 'Latvia', 'Lithuania');

"""
Counting the countries of each continent
6.
For each continent show the continent and number of countries.
"""
SELECT continent, COUNT(name)
FROM world
GROUP BY continent;

"""
Counting big countries in each continent
7.
For each continent show the continent and number of countries with populations of at least 10 million.
"""
SELECT continent, COUNT(name)
FROM world
WHERE population >= 10000000
GROUP BY continent;

"""
Counting big continents
8.
List the continents that have a total population of at least 100 million.
"""
SELECT continent
FROM world
GROUP BY continent
HAVING SUM(population) >= 100000000;

"""
9.
Show winners who have won more than one subject.

nobel(yr, subject, winner) 
"""
SELECT winner FROM nobel
GROUP BY winner
HAVING COUNT(DISTINCT subject) > 1;

"""
GROUP BY yr, subject

10.
Show the year and subject where 3 prizes were given. Show only years 2000 onwards.

nobel(yr, subject, winner)  
"""
SELECT yr, subject
FROM nobel
WHERE yr >= 2000
GROUP BY yr, subject
HAVING COUNT(winner) = 3;
