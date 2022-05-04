import json
import os
import pathlib
import uuid
import requests
from constants import *
from api.endpoints.endpoints import *


class ApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Requests/' + requests.__version__,
            'Origin': 'https://target.my.com',
            'Referer': 'https://target.my.com/'
        }

    def request(self, method, url, data=None, json=None, files=None):
        return self.session.request(method, url, data=data, json=json, files=files, headers=self.headers)

    def post_login(self):
        data = {
            'email': EMAIL,
            'password': PASSWORD,
            'continue': CONTINUE_AUTH,
            'failure': FAILURE_AUTH
        }

        self.request('POST', LOGIN_AUTH, data=data)
        self.session.request('GET', LOGIN_CSRF, headers=self.headers)
        self.headers['X-CSRFToken'] = self.session.cookies.get_dict()['csrftoken']

    def post_search_phrase(self):
        data = {
            'phrases': 'Chuchelo Myauchelo from FFXIV',
        }
        return self.request('POST',
                            SEARCH_PHRASE(str(uuid.uuid4())),
                            data=data)

    def post_create_segment(self, phrase):
        script_path = os.path.dirname(os.path.abspath(__file__))
        dir_path = pathlib.Path(script_path).parent
        file_path = str(pathlib.Path(dir_path, 'api', 'samples', 'remarketing_segments.json'))
        with open(file_path) as file:
            data_json = json.load(file)

        data_json['name'] = str(uuid.uuid4())
        data_json['relations'][0]['params']['source_id'] = phrase['id']

        return self.request('POST',
                            CREATE_SEGMENT,
                            json=data_json)

    def delete_segment(self, segment_id):
        return self.request('DELETE',
                            DELETE_SEGMENT(segment_id))

    def get_segment(self, segment_id):
        return self.request('GET',
                            GET_SEGMENT(segment_id))

    def get_create_campaign_url(self):
        target_url = 'https://eu.finalfantasyxiv.com/lodestone/character/21642366/'
        return self.request('GET', CREATE_CAMPAIGN_URL(target_url))

    def post_create_campaign_image(self):
        script_path = os.path.dirname(os.path.abspath(__file__))
        dir_path = pathlib.Path(script_path).parent
        file_path = str(pathlib.Path(dir_path, 'api', 'samples', 'my_ffxiv_character.jpg'))

        with open(file_path, 'rb') as file:
            files = {"file": file}
            return self.request('POST', CREATE_CAMPAIGN_IMAGE, files=files)

    def post_create_campaign(self, url_id, image_id):
        script_path = os.path.dirname(os.path.abspath(__file__))
        dir_path = pathlib.Path(script_path).parent
        file_path = str(pathlib.Path(dir_path, 'api', 'samples', 'campaigns.json'))
        with open(file_path) as file:
            data_json = json.load(file)

        data_json['name'] = str(uuid.uuid4())
        data_json['package_id'] = 961  # не меняется, зависит от настроек кампании
        data_json['banners'][0]['urls']['primary']['id'] = url_id
        data_json['banners'][0]['content']['image_240x400']['id'] = image_id

        return self.request('POST',
                            'https://target.my.com/api/v2/campaigns.json', json=data_json)

    def get_campaign(self, campaign_id):
        return self.request('GET',
                            GET_CAMPAIGN(campaign_id))

    def delete_campaign(self, campaign_id):
        return self.request('DELETE',
                            DELETE_CAMPAIGN(campaign_id))
