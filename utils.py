import os
import sqlite3
import time

def history_log(action, sonarrSeriesId, sonarrEpisodeId, description):
    # Open database connection
    db = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'data/db/bazarr.db'), timeout=30)
    c = db.cursor()

    # Get Sonarr API URL from database config table
    history = c.execute('''INSERT INTO table_history(action, sonarrSeriesId, sonarrEpisodeId, timestamp, description) VALUES (?, ?, ?, ?, ?)''', (action, sonarrSeriesId, sonarrEpisodeId, time.time(), description))

    # Commit changes to DB
    db.commit()
    
    # Close database connection
    db.close()
