import pytest
import psycopg2

from ..config import get_config
from ..models import Session



@pytest.fixture
def config():
    return get_config()


def test_configuration(config):
    assert "database" in config
    assert "conn_str" in config.database


def test_connection(config):
    config = get_config()
    psycopg2.connect(config.database.conn_str)
