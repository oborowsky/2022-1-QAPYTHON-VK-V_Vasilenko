import pytest

from api.client import ApiClient


class BaseCase:
    api_client = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.api_client = ApiClient()
        self.api_client.post_login()

    def create_segment(self):
        phrase = self.api_client.post_search_phrase().json()
        return self.api_client.post_create_segment(phrase).json()['id']

    def delete_segment(self, segment_id):
        return self.api_client.delete_segment(segment_id)

    def status_segment(self, segment_id):
        return self.api_client.get_segment(segment_id).json()['items'][0]['status']

    def create_url_id(self):
        return self.api_client.get_create_campaign_url().json()['id']

    def create_image_id(self):
        return self.api_client.post_create_campaign_image().json()['id']

    def create_campaign(self, url_id, image_id):
        return self.api_client.post_create_campaign(url_id, image_id).json()['id']

    def delete_campaign(self, campaigns_id):
        return self.api_client.delete_campaign(campaigns_id).status_code == 204

    def check_campaign(self, campaigns_id):
        return len(self.api_client.get_campaign(campaigns_id).json()['items']) > 0
