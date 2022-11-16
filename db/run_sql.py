import logging

import psycopg2
import psycopg2.extras as ext

DBNAME = 'stockready'

logger = logging.getLogger(__name__)

def run_sql(sql, values = None, do_fetchall = True):
    conn = None
    cur = None
    results = []

    try:
        # Connect to the DB
        conn = psycopg2.connect(f"dbname='{DBNAME}'")
        # Define a dictionary cursor ---
        # `results` will be a list of dictionaries
        cur = conn.cursor(cursor_factory = ext.DictCursor)
        # Print a trace 
        logger.debug("SQL: %s", cur.mogrify(sql, values))
        # Execute the SQL
        cur.execute(sql, values)
        # Commit transaction
        conn.commit()
        # Fetch the results, unless parameter overriden to False
        if do_fetchall:
            results = cur.fetchall()
    finally:
        # Close the cursor
        if cur is not None:
            cur.close()
        # Close the connection
        if conn is not None:
            conn.close()

    return results