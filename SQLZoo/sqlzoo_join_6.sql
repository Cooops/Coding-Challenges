-- SQL ZOO practice questions @ 11/26/2018
-- http://sqlzoo.net/w/index.php/More_JOIN_operations

"""
Star Trek movies
3.
List all of the Star Trek movies, include the id, title and yr (all of these movies include the words Star Trek in the title). Order results by year.
"""
SELECT id, title, yr
FROM movie
WHERE title LIKE ('Star Trek%')
ORDER BY yr;

"""
id for actor Glenn Close
4.
What id number does the actor 'Glenn Close' have?
"""
SELECT id
FROM actor
WHERE name = 'Glenn Close';

"""
id for Casablanca
5.
What is the id of the film 'Casablanca'
"""
SELECT id
FROM movie
WHERE title = 'Casablanca';

"""
Cast list for Casablanca
6.
Obtain the cast list for 'Casablanca'.

what is a cast list?
The cast list is the names of the actors who were in the movie.

Use movieid=11768, (or whatever value you got from the previous question)
"""
SELECT actor.name
FROM actor
JOIN casting ON casting.actorid = actor.id
WHERE casting.movieid = 11768;

"""
Alien cast list
7.
Obtain the cast list for the film 'Alien'
"""
SELECT actor.name
FROM actor
JOIN casting ON casting.actorid = actor.id
JOIN movie ON movie.id = casting.movieid
WHERE movie.title = 'Alien';

"""
Harrison Ford movies
8.
List the films in which 'Harrison Ford' has appeared
"""
SELECT movie.title
FROM movie
JOIN casting ON casting.movieid = movie.id
JOIN actor ON actor.id = casting.actorid
WHERE actor.name = 'Harrison Ford';

"""
Harrison Ford as a supporting actor
9.
List the films where 'Harrison Ford' has appeared - but not in the starring role.

Note: the ord field of casting gives the position of the actor. If ord=1 then this actor is in the starring role
"""
SELECT movie.title
FROM movie
JOIN casting ON casting.movieid = movie.id
JOIN actor ON actor.id = casting.actorid
WHERE actor.name = 'Harrison Ford'
AND casting.ord != 1;

"""
Lead actors in 1962 movies
10.
List the films together with the leading star for all 1962 films.
"""
SELECT movie.title, actor.name
FROM movie
JOIN casting on casting.movieid = movie.id
JOIN actor ON actor.id = casting.actorid
WHERE casting.ord = 1
AND movie.yr = 1962;

"""
Harder Questions

Busy years for John Travolta
11.
Which were the busiest years for 'John Travolta', show the year and the number of movies he made each year for any year in which he made more than 2 movies.
"""
SELECT yr, COUNT(title)
FROM movie
JOIN casting ON movie.id = casting.movieid
JOIN actor ON casting.actorid = actor.id
WHERE name = 'John Travolta'
GROUP BY yr
HAVING COUNT(title) = (
    SELECT MAX(c) FROM (
        SELECT yr, COUNT(title) AS c
        FROM movie
        JOIN casting ON movie.id = casting.movieid
        JOIN actor ON casting.actorid = actor.id
        WHERE name = 'John Travolta'
        GROUP BY yr) AS t
);

"""
Lead actor in Julie Andrews movies
12.
List the film title and the leading actor for all of the films 'Julie Andrews' played in.

Did you get "Little Miss Marker twice"?
Julie Andrews starred in the 1980 remake of Little Miss Marker and not the original(1934).

Title is not a unique field, create a table of IDs in your subquery

https://www.youtube.com/watch?v=BcNIDK5qYx8
"""
SELECT movie.title, name
FROM movie
JOIN casting ON (movie.id = casting.movieid AND casting.ord =1)
JOIN actor ON casting.actorid = actor.id
WHERE movie.id IN (
    SELECT casting.movieid
    FROM casting
    WHERE casting.actorid IN (
        SELECT actor.id
        FROM actor
        WHERE name='Julie Andrews')
);
"""
Actors with 30 leading roles
13.
Obtain a list, in alphabetical order, of actors who've had at least 30 starring roles.
"""
SELECT name
FROM actor
JOIN casting ON (id = actorid AND (
    SELECT COUNT(ord)
    FROM casting
    WHERE casting.actorid = actor.id AND ord = 1) >= 30)
GROUP BY name;
