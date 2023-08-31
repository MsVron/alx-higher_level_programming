-- This script presents a list of all TV shows stored in hbtn_0d_tvshows
-- that are associated with at least one genre.

-- Employing a join operation to display data and sorting by title and genre id.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
