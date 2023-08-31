-- This script displays a list of all shows in the hbtn_0d_tvshows database without the genre Comedy.

-- Utilizing an inner join and a subquery to connect multiple tables.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
    SELECT tv_shows.title
    FROM tv_shows
    JOIN tv_show_genres
    ON tv_show_genres.show_id = tv_shows.id
    JOIN tv_genres
    ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title;
