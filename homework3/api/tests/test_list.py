import pytest

from api.tests.base import BaseCase


class TestMyTarget(BaseCase):

    @pytest.mark.API
    def test_create_segment(self):
        segment_id = self.create_segment()
        status = self.status_segment(segment_id)
        assert status == 'processing' or status == 'ready'

    @pytest.mark.API
    def test_delete_segment(self):
        segment_id = self.create_segment()
        self.delete_segment(segment_id)
        status = self.status_segment(segment_id)
        assert status == 'not found'

    @pytest.mark.API
    def test_campaigns(self):
        campaigns_id = self.create_campaign()
        assert self.check_campaign(campaigns_id) and self.delete_campaign(campaigns_id)
