-- SQL ZOO practice questions @ 11/25/2018
-- https://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial

"""
Bigger than Russia
1.
List each country name where the population is larger than that of 'Russia'.

world(name, continent, area, population, gdp)
"""
SELECT name
FROM world
WHERE population > (SELECT population FROM world WHERE name='Russia');

"""
Richer than UK
2.
Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.

Per Capita GDP
The per capita GDP is the gdp/population
"""
SELECT name
FROM world
WHERE continent = 'Europe'
AND gdp/population > (SELECT gdp/population FROM world WHERE name = 'United Kingdom');

"""
Neighbours of Argentina and Australia
3.

List the name and continent of countries in the continents containing either Argentina or Australia. Order by name of the country.
"""
SELECT name, continent
FROM world
WHERE continent IN (SELECT continent FROM world WHERE name in ('Argentina', 'Australia'))
ORDER by name;

"""
Between Canada and Poland
4.
Which country has a population that is more than Canada but less than Poland? Show the name and the population.
"""
SELECT name, population
FROM world
WHERE population > (SELECT population FROM world WHERE name = 'Canada')
AND population < (SELECT population FROM world WHERE name = 'Poland');

"""
Percentages of Germany
5.
Germany (population 80 million) has the largest population of the countries in Europe. Austria (population 8.5 million) has 11% of the population of Germany.

Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.

Decimal places
You can use the function ROUND to remove the decimal places.
Percent symbol %
You can use the function CONCAT to add the percentage symbol.
"""
SELECT name, CONCAT(ROUND(population/(SELECT population FROM world WHERE name ='Germany')*100), '%')
FROM world
WHERE continent = 'Europe';
