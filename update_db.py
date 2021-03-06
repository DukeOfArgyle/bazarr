import os
import sqlite3

# Check if database exist
if os.path.exists(os.path.join(os.path.dirname(__file__), 'data/db/bazarr.db')) == True:
    # Open database connection
    db = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'data/db/bazarr.db'), timeout=30)
    c = db.cursor()
    
    # Execute tables modifications
    try:
        c.execute('alter table table_settings_providers add column "username" "text"')
    except:
        pass
    else:
        c.execute('UPDATE table_settings_providers SET username=""')

    try:
        c.execute('alter table table_settings_providers add column "password" "text"')
    except:
        pass
    else:
        c.execute('UPDATE table_settings_providers SET password=""')

    try:
        c.execute('alter table table_shows add column "audio_language" "text"')
    except:
        pass

    try:
        c.execute('alter table table_settings_general add column "configured" "integer"')
        c.execute('alter table table_settings_general add column "updated" "integer"')
    except:
        pass

    try:
        c.execute('alter table table_settings_general add column "single_language" "text"')
    except:
        pass
    else:
        c.execute('UPDATE table_settings_general SET single_language="False"')

    try:
        c.execute('CREATE TABLE `table_settings_notifier` (`name` TEXT, `url` TEXT, `enabled` INTEGER);')
    except:
        pass
    else:
        providers = ['Boxcar','Faast','Growl','Join','KODI','Mattermost','Notify My Android','Prowl','Pushalot','PushBullet','Pushjet','Pushover','Rocket.Chat','Slack','Super Toasty','Telegram','Twitter','XBMC']
        for provider in providers:
            c.execute('INSERT INTO `table_settings_notifier` (name, enabled) VALUES (?, ?);', (provider,'0'))

    # Commit change to db
    db.commit()

    # Close database connection
    db.close()
