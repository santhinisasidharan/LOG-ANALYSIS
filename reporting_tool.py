#!/usr/bin/env python
import psycopg2

DBNAME = "news"


def three_most_popular_articles():
    '''This function prints the three most popular articles of all
    time in descending order'''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('SELECT title, views FROM popular_article_details'
              ' ORDER BY views DESC limit 3;')
    return c.fetchall()
    db.close()


def most_popular_authors():
    '''This function prints the most popular authors based on summed
    up views for all articles by that author'''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT name, total_views FROM popular_authors;")
    return c.fetchall()
    db.close()


def more_than_one_percent_error():
    '''This function prints the dates where
    more than 1% request lead to errors.The log table includes
    a column status that indicates the HTTP status code,
    that the news site sent to the user's browser.'''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('SELECT date, CAST(percentage_error AS DECIMAL(10,2))'
              ' FROM percent_error_table;')
    return c.fetchall()
    db.close()


def reporting_tool():
    #   Reporting top 3 most popular articles
    print " "
    print "POPULAR ARTICLES "
    print "****************"
    print " "
    n = 1
    for each in three_most_popular_articles():
        print str(n) + ". " + str(each[0]) + " --- " + str(each[1]) + " views."
        n = n + 1
    print " "
    # Reporting authors based on popularity of their articles
    print "POPULAR AUTHORS"
    print "***************"
    print " "
    n = 1
    for each in most_popular_authors():
        print str(n) + ". " + each[0] + " --- " + str(each[1]) + " views."
        n = n + 1
    print " "
    # Reporting dates where more than 1% request lead to errors
    print "ERROR LOG "
    print "*********"
    print " "
    for each in more_than_one_percent_error():
        print str(each[0]) + " --- " + str(each[1]) + " % "


reporting_tool()
