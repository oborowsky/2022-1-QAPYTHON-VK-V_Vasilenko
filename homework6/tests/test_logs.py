import pytest

from tests.base_test import BaseTest
from models.models import *


class TestLogs(BaseTest):
    def get_table(self, model):
        self.mysql.session.commit()
        res = self.mysql.session.query(model)
        return res.all()

    @pytest.mark.parametrize(
        'model', [
            TotalAmountRequestsModel,
            AmountByTypeRequestsModel,
            Top10FrequentRequestsModel,
            Top5LargestRequestsWithClientErrorModel,
            Top5FrequentRequestsWithServerErrorModel
        ])
    def test_banners(self, model):
        table = self.builder.create_table(model)
        count = self.get_table(model)
        assert len(count) == table.expected_value
