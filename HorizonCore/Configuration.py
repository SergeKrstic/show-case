from decouple import config

# User IDs that sunny will messages to
Users = [
    {'Name': config('USER_NAME'),
     'UserId': 'Rwc20oNDgKQ32bwVOOKbPYzndrG3',
     'MessengerId': config('MESSENGER_ID_FOR_USER'),
     'TimeZoneOffset': 11,  # AEST: +10 , AEDT: +11
     'QuotesEnabled': True,
     'QuoteDictionary': None},
]

AdminId = Users[0]['MessengerId']
