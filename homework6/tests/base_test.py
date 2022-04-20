import pytest
from mysql.client import MysqlClient
from utils.builder import MysqlBuilder


class BaseTest:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.mysql)
        self.prepare()
