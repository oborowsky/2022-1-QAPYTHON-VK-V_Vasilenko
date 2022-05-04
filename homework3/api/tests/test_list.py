import pytest

from api.tests.base import BaseCase


class TestMyTarget(BaseCase):

    @pytest.mark.API
    def test_create_segment(self):
        segment_id = self.create_segment()
        status = self.status_segment(segment_id)
        self.delete_segment(segment_id)
        assert status in ['processing', 'ready']

    @pytest.mark.API
    def test_delete_segment(self):
        segment_id = self.create_segment()
        self.delete_segment(segment_id)
        status = self.status_segment(segment_id)
        assert status == 'not found'

    @pytest.mark.API
    def test_create_campaign(self):
        url_id = self.create_url_id()
        image_id = self.create_image_id()
        campaigns_id = self.create_campaign(url_id, image_id)
        check = self.check_campaign(campaigns_id)
        self.delete_campaign(campaigns_id)
        assert check

    @pytest.mark.API
    def test_delete_campaign(self):
        url_id = self.create_url_id()
        image_id = self.create_image_id()
        campaigns_id = self.create_campaign(url_id, image_id)
        assert self.delete_campaign(campaigns_id)
