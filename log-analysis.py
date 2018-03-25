#!/usr/bin/env python3
import psycopg2

# Connect to the database
db = psycopg2.connect("dbname=news")

question_one = "What are the most popular three articles of all time?"
question_two = "Who are the most popular article authors of all time?"
question_three = "On which days did more than 1% of requests lead to errors?"

# Open a cursor to perform database operations
cur = db.cursor()

# Questions used for the project
question_one = "What are the most popular three articles of all time?"
question_two = "Who are the most popular article authors of all time?"
question_three = "On which days did more than 1% of requests lead to errors?"

# Construction of the queries used to answer the questions
query = ("""
    SELECT Title, count(path) as Views
    FROM articles, log
    WHERE log.path like concat('%', articles.slug)
    GROUP BY title, path
    ORDER BY Views desc
    LIMIT 3;
    """)

query2 = ("""
    SELECT name, count(path) as views
    FROM authors, articles, log
    WHERE log.path like concat('%', articles.slug)
    and authors.id = articles.author
    GROUP BY name
    ORDER BY views desc;
    """)

query3 = ("""
    SELECT TO_CHAR(tbl.date, 'Mon DD, YYYY') AS formatedDate,
    TO_CHAR(tbl.error_percent, 'FM99.99%') AS percentage
    FROM view_error_percent AS tbl
    WHERE tbl.error_percent > 1
    ORDER BY tbl.error_percent DESC;
    """)


def print_results(question, query, error=False):
    """
    Function that prints out the results of a given query
    Inputs are as follows:
        Question: Question variable as string
        Query: A query used to answer question
        Error: Set to true if question involve errors
    """
    print(question)
    print("")
    cur.execute(query)
    query = cur.fetchall()
    for key, result in query:
        if error is False:
            print('{:<32} - {:>9} views'.format(key, str(result)))
        if error:
            print('{:<32} - {:>9} error rate'.format(key, str(result)))

    print("")
    print("-"*60)
    print("")


if __name__ == '__main__':
    # Print out all the results
    print("="*60)
    print_results(question_one, query)
    print_results(question_two, query2)
    print_results(question_three, query3, True)

    # Close communication with the database
    cur.close()
    db.close()
