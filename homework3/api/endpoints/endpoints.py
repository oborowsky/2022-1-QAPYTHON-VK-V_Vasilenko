LOGIN_AUTH = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
LOGIN_CSRF = 'https://target.my.com/csrf/'


def SEARCH_PHRASE(phrase_name):
    return f'https://target.my.com/api/v3/search_phrases.json?name={phrase_name}'


CREATE_SEGMENT = 'https://target.my.com/api/v2/remarketing/segments.json'


def DELETE_SEGMENT(segment_id):
    return f'https://target.my.com/api/v2/remarketing/segments/{str(segment_id)}.json'


def GET_SEGMENT(segment_id):
    return f'https://target.my.com/api/v2/coverage/segment.json?id={str(segment_id)}'


CREATE_CAMPAIGN = 'https://target.my.com/api/v2/campaigns.json'


def DELETE_CAMPAIGN(campaign_id):
    return f'https://target.my.com/api/v2/campaigns/{campaign_id}.json'


def GET_CAMPAIGN(campaign_id):
    return f'https://target.my.com/api/v2/campaigns.json?_id={campaign_id}'
