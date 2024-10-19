USE pa03;

CREATE USER 'users_reader'@'localhost' IDENTIFIED BY '123456Aa@';
GRANT SELECT ON users TO 'users_reader'@'localhost';
SHOW GRANTS FOR 'users_reader'@'localhost';

CREATE USER 'movies_reader'@'localhost' IDENTIFIED BY '123456Aa@';
GRANT SELECT ON movies TO 'movies_reader'@'localhost';
SHOW GRANTS FOR 'movies_reader'@'localhost';

CREATE USER 'users&watchlists_reader'@'localhost' IDENTIFIED BY '123456Aa@';
GRANT SELECT ON users TO 'users&watchlists_reader'@'localhost';
GRANT SELECT ON watchlists TO 'users&watchlists_reader'@'localhost';
SHOW GRANTS FOR 'users&watchlists_reader'@'localhost';
