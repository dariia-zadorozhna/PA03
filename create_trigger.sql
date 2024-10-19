-- for this trigger I needed to create a new table
create table user_activity_log (
    id int auto_increment primary key,
    user_id int not null,
    action varchar(50) not null,
    movie_id int,
    action_time timestamp default current_timestamp,
    foreign key (user_id) references users(id),
    foreign key (movie_id) references movies(id)
);

delimiter //

create trigger after_movie_genre_insert
after insert on moviegenres
for each row
begin
    update genres
    set movie_count = movie_count + 1
    where id = new.genre_id;
end //

delimiter ;