import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_db_connection():
    """
    Create a database connection to the MySQL database specified by the db_name.

    Returns
    -------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        print("MySQL Database connection successful")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def execute_query(connection, query, data=None):
    """
    Execute a given SQL query on the provided database connection.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    query : str
        The SQL query to execute.
    data : tuple, optional
        The data tuple to pass to the query, for parameterized queries.

    Returns
    -------
    None
    """
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_category(connection, name, description):
    """
    Inserts a new category into the categories table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the category.
    description : str
        The description of the category.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO categories (name, description)
    VALUES (%s, %s)
    """
    data = (name, description)
    execute_query(connection, query, data)

def insert_reporter(connection, name, email):
    """
    Inserts a new reporter into the reporters table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the reporter.
    email : varchar
        The email of the reporter.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO reporters (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    execute_query(connection, query, data)

def insert_publisher(connection, name, email):
    """
    Inserts a new publisher into the publishers table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the publisher.
    email : varchar
        The email of the publisher.
    phone_number : int
        The phone_number of the publisher.
    head_office_address : varchar
        The head_office_address of the publisher.
    facebook : varchar
        The facebook of the publisher.
    twitter : varchar
        The twitter of the publisher.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO publishers (name, email, phone_number, head_office_address, facebook, twitter)
    VALUES (%s, %s, %d, %s, %s, %s)
    """
    data = (name, email, phone_number, head_office_address, facebook, twitter)
    execute_query(connection, query, data)

def insert_news(connection, category_id, reporter_id, publisher_id, datetime, title, body, link):
    """
    Inserts a new news article into the news table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    category_id : int
        The ID of the category.
    reporter_id : int
        The ID of the reporter.
    publisher_id : int
        The ID of the publisher.
    datetime : datetime
        The publication date and time of the news article.
    title : str
        The title of the news article.
    body : str
        The body text of the news article.
    link : str
        The URL link to the full news article.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO news (category_id, reporter_id, publisher_id, datetime, title, body, link)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (category_id, reporter_id, publisher_id, datetime, title, body, link)
    execute_query(connection, query, data)

def insert_image(connection, news_id, image_url):
    """
    Inserts a new image into the images table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    news_id : int
        The ID of the news article associated with the image.
    image_url : str
        The URL of the image.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO images (news_id, image_url)
    VALUES (%s, %s)
    """
    data = (news_id, image_url)
    execute_query(connection, query, data)

def insert_summary(connection, news_id, summary_text):
    """
    Inserts a new summary into the summaries table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    news_id : int
        The ID of the news article associated with the summary.
    summary_text : str
        The text of the summary.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO summaries (news_id, summary_text)
    VALUES (%s, %s)
    """
    data = (news_id,  summary_text)
    execute_query(connection, query, data)

# Example usage
if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:
        insert_category(conn, "Politics", "All news related to politics")
        insert_reporter(conn, "jonny" , "jonny@mial.com")
        insert_news(conn, "4","4","1", "2024-05-08 23:29","Head, Abishek power Hyderabad to victory over Lucknow inside 10 overs",
                    """Openers Travis Head and Abhishek Sharma smoked half-centuries as Sunrisers Hyderabad crushed Lucknow Super Giants by 10 wickets on Wednesday 
                    to boost their play-off hopes in the IPL.""", 
                    "https://www.thedailystar.net/sports/cricket/news/head-abishek-power-hyderabad-victory-over-lucknow-inside-10-overs-3605301")
        
        insert_image( conn, "1", "https://tds-images.thedailystar.net/sites/default/files/styles/big_202/public/images/2024/05/08/afp_20240508_34r89pa_v1_preview_cricketindiplt20hyderabadlucknow.jpg")
        insert_summary(conn, "2" , """ a weather bulletin issued this morning.The country's maximum temperature yesterday was recorded at 35 degrees Celsius at Khepupara.""")
        
        # Add more insert calls for other tables
