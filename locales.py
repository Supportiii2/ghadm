from locales_dict import Locale, LocalesDict

locale_en = Locale()
locale_de = Locale()

locales = LocalesDict({
    'en': locale_en,
    'de': locale_de
}, locale_en)

# TOO_LONG_TITLE
locale_en.too_long_title = 'Your message is too long'
locale_de.too_long_title = 'Die Nachricht ist zu lang'

# FOR_TITLE
locale_en.for_title = 'For %s'
locale_de.for_title = 'Für %s'

# EXCEPT_TITLE
locale_en.except_title = 'Except %s'
locale_de.except_title = 'Nicht für %s'

# SPOILER_TITLE
locale_en.spoiler_title = 'ADM message'
locale_de.spoiler_title = 'ADM Nachricht'

# TOO_LONG_MESSAGE
locale_en.too_long_message = '🥺 Sorry, your message can\'t be sent as it exceeds the limit of 200 characters.'
locale_de.too_long_message = '🥺 Tut mir leid, deine Nachricht kann nicht gesendet werden, da sie die Grenze von 200 Zeichen überschreitet.'

# FOR_MESSAGE
locale_en.for_message = 'Private message for %s.'
locale_de.for_message = 'Private Nachricht für %s.'

# EXCEPT_MESSAGE
locale_en.except_message = 'Private message for everyone except %s.'
locale_de.except_message = 'Private Nachricht für alle außer %s.'

# SPOILER_MESSAGE
locale_en.spoiler_message = '📨 A message to GroupHelp admins:'
locale_en.spoiler_message = '📨 Eine Nachricht an GroupHelp Admins:'

# GROUP_GREETING_MESSAGE
locale_en.group_greeting_message = '👋 Hello! This bot is exclusively for communication between @GroupHelp admins.'
locale_de.group_greeting_message = '👋 Hallo! Dieser Bot ist ausschließlich für die Kommunikation zwischen @GroupHelp-Administratoren gedacht.'

# INFO_MESSAGE
locale_en.info_message = '👋 Hello! This bot is exclusively for communication between @GroupHelp admins.'
locale_de.info_message = '👋 Hallo! Dieser Bot ist ausschließlich für die Kommunikation zwischen @GroupHelp-Administratoren gedacht.'

# TOO_LONG_DESCRIPTION
locale_en.too_long_description = 'Please shorten the length of your message so that it doesn\'t exceed the limit of 200 characters.'
locale_en.too_long_description = 'Bitte kürze die Länge deiner Nachricht so, dass sie die Grenze von 200 Zeichen nicht überschreitet.'

# NOT_ALLOWED
locale_en.not_allowed = 'You are not a GroupHelp Admin!'
locale_de.not_allowed = 'Du bist kein GroupHelp Admin!'

# NOT_ACCESSIBLE
locale_en.not_accessible = 'This content is no longer accessible.'
locale_de.not_accessible = 'Inhalt kann nicht angezeigt werden.'

# VIEW
locale_en.view = '👀 View'
locale_de.view = '👀 Ansehen'

# AND_CONNECTOR
locale_en.and_connector = 'and'
locale_en.and_connector = 'und'

#ADMIN_MESSAGE
locale_en.admin_message = ('Here is how to use this bot:'
                           'tlgrmde.ml/ghadm')
                          

