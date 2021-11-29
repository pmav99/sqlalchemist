import pytest
import psycopg2

from sqlalchemist import get_config


@pytest.fixture
def config():
    return get_config()


def test_configuration(config):
    assert "database" in config
    assert "DB_CONNECTION_STRING" in config.database


def test_connection(config):
    config = get_config()
    psycopg2.connect(config.database.DB_CONNECTION_STRING)
