from locales_dict import Locale, LocalesDict

locale_en = Locale()

locales = LocalesDict({
    'en': locale_en
}, locale_en)

# TOO_LONG_TITLE
locale_en.too_long_title = 'Your message is too long'

# FOR_TITLE
locale_en.for_title = 'For %s'

# EXCEPT_TITLE
locale_en.except_title = 'Except %s'

# SPOILER_TITLE
locale_en.spoiler_title = 'ADM Messaggio'

# TOO_LONG_MESSAGE
locale_en.too_long_message = '🥺 Sorry, your message can\'t be sent as it exceeds the limit of 200 characters.'

# FOR_MESSAGE
locale_en.for_message = 'Private message for %s.'

# EXCEPT_MESSAGE
locale_en.except_message = 'Private message for everyone except %s.'

# SPOILER_MESSAGE
locale_en.spoiler_message = '📨 A message to GroupHelp admins:'

# GROUP_GREETING_MESSAGE
locale_en.group_greeting_message = '👋 Hello! This bot is exclusively for communication between @GroupHelp admins.'

# INFO_MESSAGE
locale_en.info_message = '👋 Hello! This bot is exclusively for communication between @GroupHelp admins.'

# TOO_LONG_DESCRIPTION
locale_en.too_long_description = 'Please shorten the length of your message so that it doesn\'t exceed the limit of 200 characters.'

# NOT_ALLOWED
locale_en.not_allowed = 'You are not a GroupHelp Admin!'

# NOT_ACCESSIBLE
locale_en.not_accessible = 'This content is no longer accessible.'

# VIEW
locale_en.view = '👀 View'

# AND_CONNECTOR
locale_en.and_connector = 'and'
