create view users_watched_movies as
select users.first_name as user_first_name, users.last_name as user_last_name, movies.title as movie_title, genres.name as movie_genre
from watchlists w
join users on w.user_id = users.id
join movies on w.movie_id = movies.id
join moviegenres on w.movie_id = moviegenres.movie_id
join genres on moviegenres.genre_id = genres.id;