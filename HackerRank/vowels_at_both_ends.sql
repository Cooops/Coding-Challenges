# https://www.hackerrank.com/challenges/weather-observation-station-8/problem

"""
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. 
Your result cannot contain duplicates.
"""
SELECT DISTINCT city
FROM station 
WHERE LEFT(city, 1) IN ('a','e','i','o','u') -- pops out the first element in the string (city) and checks if it is in our list of vowels
AND RIGHT(city, 1) IN ('a','e','i','o','u'); -- same thing for the last element in the string
