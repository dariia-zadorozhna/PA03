create table if not exists users (
	id int primary key,
	first_name varchar(100) not null,
	last_name varchar(100) not null,
	email varchar(100) not null,
	phone varchar(100) not null,
	password_hash varchar(255) not null,
	join_date timestamp default current_timestamp
)

alter table users
comment = 'Table to store user information';

alter table users
modify column id int comment 'unique identifier for each user',
modify column first_name varchar(100) not null comment 'first name of the user',
modify column last_name varchar(100) not null comment 'last name of the user',
modify column email varchar(100) not null comment 'email address of the user',
modify column phone varchar(100) not null comment 'phone number of the user',
modify column password_hash varchar(255) not null comment 'password hash of the user',
modify column join_date timestamp default current_timestamp comment 'the date of user join';


create table if not exists userprofiles (
	id int primary key,
	user_id int unique not null,
	bio text,
	foreign key(user_id) references users(id)
)

alter table userprofiles
comment = 'table to store additional user information such as biographies and profile details';

alter table userprofiles
modify column id int comment 'unique identifier for each user profile',
modify column user_id int unique not null comment 'reference to the associated user in the users table',
modify column bio text comment 'short biography or description provided by the user';

create table if not exists movies (
	id int primary key,
	title varchar(100) not null,
	release_year int not null,
	duration int not null,
	index (release_year)
)

alter table movies
modify column id int comment 'unique identifier for each movie',
modify column title varchar(100) not null comment 'title of the movie',
modify column release_year int not null comment 'year the movie was released',
modify column duration int not null comment 'duration of the movie in minutes',
add index (release_year) comment 'index to optimize queries filtering by release year',
comment = 'table to store information about movies including title, release year, and duration';

create table if not exists genres (
	id int primary key,
	name varchar(30) not null
)

alter table genres
modify column id int comment 'unique identifier for each genre',
modify column name varchar(30) not null comment 'name of the genre',
comment = 'table to store different movie genres such as action, drama, or comedy';

create table if not exists movieGenres (
		movie_id int not null,
		genre_id int not null,
		primary key (movie_id, genre_id),
		foreign key (movie_id) references movies(id),
		foreign key (genre_id) references genres(id)
)

alter table moviegenres
modify column movie_id int not null comment 'reference to the associated movie in the movies table',
modify column genre_id int not null comment 'reference to the associated genre in the genres table',
comment = 'table to store the relationship between movies and genres, allowing a movie to have multiple genres and a genre to belong to multiple movies';


create table if not exists reviews (
	id int primary key,
	user_id int not null,
	movie_id int not null,
	rating int check (rating between 1 and 5),
	review_text text,
	review_date timestamp default current_timestamp,
	foreign key(user_id) references users(id),
	foreign key(movie_id) references movies(id),
	unique (user_id,movie_id)
)

alter table reviews
modify column id int comment 'unique identifier for each review',
modify column user_id int not null comment 'reference to the user who submitted the review',
modify column movie_id int not null comment 'reference to the reviewed movie',
modify column rating int check (rating between 1 and 5) comment 'rating given by the user, from 1 to 5',
modify column review_text text comment 'optional text review provided by the user',
modify column review_date timestamp default current_timestamp comment 'timestamp of when the review was submitted',
comment = 'table to store reviews submitted by users, with ratings and optional text';


create table if not exists watchlists(
	id int primary key,
	user_id int not null,
	movie_id int not null,
	added_date timestamp default current_timestamp,
	foreign key (user_id) references users(id),
	foreign key (movie_id) references movies(id),
	unique (user_id,movie_id)
)

alter table watchlists
modify column id int comment 'unique identifier for each watchlist entry',
modify column user_id int not null comment 'reference to the user who added the movie to their watchlist',
modify column movie_id int not null comment 'reference to the movie added to the watchlist',
modify column adedd_date timestamp default current_timestamp comment 'timestamp of when the movie was added to the watchlist',
comment = 'table to store movies added to users’ watchlists';
