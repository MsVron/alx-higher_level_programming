-- This script provides a list of all shows and their linked genres from the hbtn_0d_tvshows database.

-- Utilizing joins to display data and sorting by title and genre name.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
