delimiter //

create procedure getUserWatchedMovies (
    in inputUserId int,
    out userName varchar(255),
    out movieCount int
)
begin
    select concat(first_name, ' ', last_name) into userName
    from users
    where id = inputUserId;

    select count(*) into movieCount
    from watchlists
    where user_id = inputUserId;
end //

delimiter ;

set @userName = '';
set @watchedMovieCount = 0;
call GetUserWatchedMovies(8, @userName, @watchedMovieCount);
select @userName as UserName, @watchedMovieCount as WatchedMovieCount;