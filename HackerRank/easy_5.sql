# https://www.hackerrank.com/challenges/weather-observation-station-5

select min(length(lenName)), max(length(lenName)) from (select length(name) from test order by name asc) as lenName;
