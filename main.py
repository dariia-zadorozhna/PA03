import mysql.connector
from mysql.connector import Error
import random
from datetime import datetime, timedelta


def create_connection():
    return mysql.connector.connect(
        host='localhost',
        database='pa03',
        user='root',
        password='qwerty'
    )


def generate_random_data(entity, count):
    data = []
    for i in range(1, count + 1):
        if entity == "user":
            first_names = ['John', 'Jane', 'Alex', 'Emily', 'Michael', 'Sarah', 'David', 'Laura']
            last_names = ['Doe', 'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Garcia']
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            email = f"{first_name.lower()}.{last_name.lower()}@example.com"
            phone = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
            password_hash = f"hashed_password_{i}"  # Simulated hash
            join_date = generate_random_join_date(datetime(2020, 1, 1), datetime.now())
            data.append((i, first_name, last_name, email, phone, password_hash, join_date))
        elif entity == "movie":
            titles = [
                "The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction",
                "Schindler's List", "The Lord of the Rings: The Return of the King", "Forrest Gump",
                "Inception", "The Matrix", "The Good, the Bad and the Ugly", "Fight Club",
                "Star Wars: Episode IV - A New Hope", "The Empire Strikes Back", "The Avengers",
                "The Lion King", "The Silence of the Lambs", "Saving Private Ryan", "Interstellar",
                "Parasite", "Titanic"
            ]
            title = random.choice(titles)
            release_year = random.randint(1900, 2024)
            duration = random.randint(60, 240)
            data.append((i, title, release_year, duration))
        elif entity == "genre":
            genres = [
                "Action", "Comedy", "Drama", "Fantasy", "Horror",
                "Romance", "Science Fiction", "Thriller", "Mystery",
                "Adventure", "Animation", "Documentary", "Biography",
                "Family", "History", "Musical"
            ]
            name = genres[i % len(genres)]
            data.append((i, name))
    return data


def generate_random_join_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    random_seconds = random.randint(0, 86400)
    random_time = timedelta(seconds=random_seconds)
    return random_date + random_time


def insert_data(table, data):
    try:
        connection = create_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            if table == "users":
                insert_query = "INSERT INTO users (id, first_name, last_name, email, phone, password_hash, join_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            elif table == "movies":
                insert_query = "INSERT INTO movies (id, title, release_year, duration) VALUES (%s, %s, %s, %s)"
            elif table == "genres":
                insert_query = "INSERT INTO genres (id, name) VALUES (%s, %s)"
            elif table == "watchlists":
                insert_query = "INSERT INTO watchlists (id, user_id, movie_id) VALUES (%s, %s, %s)"
            elif table == "reviews":
                insert_query = "INSERT INTO reviews (id, user_id, movie_id, rating, review_text) VALUES (%s, %s, %s, %s, %s)"
            elif table == "movieGenres":
                insert_query = "INSERT INTO movieGenres (movie_id, genre_id) VALUES (%s, %s)"

            for record in data:
                cursor.execute(insert_query, record)
            connection.commit()
            print(f"{len(data)} entries inserted into {table} successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

insert_data("users", generate_random_data("user", 100000))
insert_data("movies", generate_random_data("movie", 100000))
insert_data("genres", generate_random_data("genre", 20))

def insert_watchlists_and_movie_genres(watchlist_count, movie_count, genre_count):
    try:
        connection = create_connection()
        if connection.is_connected():
            cursor = connection.cursor()

            insert_watchlist_query = "INSERT INTO watchlists (id, user_id, movie_id) VALUES (%s, %s, %s)"
            for watchlist_id in range(1, watchlist_count + 1):
                user_id = random.randint(1, 100000)
                movie_id = random.randint(1, movie_count)
                cursor.execute(insert_watchlist_query, (watchlist_id, user_id, movie_id))

            insert_movie_genre_query = "INSERT INTO movieGenres (movie_id, genre_id) VALUES (%s, %s)"
            for movie_id in range(1, movie_count + 1):
                number_of_genres = random.randint(1, 3)
                assigned_genres = random.sample(range(1, genre_count + 1), number_of_genres)
                for genre_id in assigned_genres:
                    cursor.execute(insert_movie_genre_query, (movie_id, genre_id))

            connection.commit()
            print(f"{watchlist_count} watchlist entries and genre assignments for {movie_count} movies inserted successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

insert_watchlists_and_movie_genres(100000, 100000, 20)


def insert_reviews(review_count, user_count, movie_count):
    try:
        connection = create_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            insert_query = "INSERT INTO reviews (id, user_id, movie_id, rating, review_text) VALUES (%s, %s, %s, %s, %s)"
            review_texts = [
                "Amazing movie!", "It was okay.", "I didn't like it.",
                "Best movie ever!", "Not worth the time.", "Would watch again.",
                "An absolute masterpiece!", "Average at best.", "Highly recommended!"
            ]

            for review_id in range(1, review_count + 1):
                user_id = random.randint(1, user_count)
                movie_id = random.randint(1, movie_count)
                rating = random.randint(1, 5)
                review_text = random.choice(review_texts)
                review_data = (review_id, user_id, movie_id, rating, review_text)
                cursor.execute(insert_query, review_data)

            connection.commit()
            print(f"{review_count} reviews inserted successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

insert_reviews(100000, 100000, 100000)
