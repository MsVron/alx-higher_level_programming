-- This script presents a list of all TV shows stored in hbtn_0d_tvshows that do not have a linked genre.

-- Gathering data using a left join, where the matching key on the right side is NULL.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title;
