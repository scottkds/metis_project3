import sqlite3
import re
import pandas as pd

def clean_input(value):
    """Cleans out any non-word characters and adds percent signs
    for searcing."""
    return '%' + re.sub(r'(\W|[0-9])', '', value) + '%'

def get_terms(search_term):
    """Splits a search term and retuns the first term surrounded by
    percent signs. The result is to be used in an SQL query."""
    term = search_term.split(' ')[0]
    clean_term = clean_input(term)
    return tuple([clean_term])

def query_name(cur, search_terms):
    """Returns the results of a name query."""
    full_name = get_terms(search_terms)
    results = list(cur.execute("""SELECT first_name, last_name
                                 FROM customers
                                 WHERE first_name like ?""",
                                 full_name))
    return results

def opendb(filename):
    """Opens a database and returns the connection and cursor objects."""
    con = sqlite3.connect(filename)
    return (con, con.cursor())


if __name__ == '__main__':
    con, cur = opendb("/Users/scott/test/flask/churn/customer.db")
    print(query_name(cur, "John"))
    con.close()
    c.close()
