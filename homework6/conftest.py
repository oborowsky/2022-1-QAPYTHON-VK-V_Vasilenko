import pytest
from mysql.client import MysqlClient


def pytest_configure(config):
    mysql_client = MysqlClient(host='127.0.0.1', port=3306, user='root', password='pass', db_name='TEST_SQL')

    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.recreate_tables()

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()
