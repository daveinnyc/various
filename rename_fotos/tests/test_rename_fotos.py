import pytest
import rename_fotos as rfapp


@pytest.fixture
def client():
    rfapp.app.config['TESTING'] = True

    with rfapp.app.test_client() as client:
        with rfapp.app.app_context():
            rfapp.init_db()
        yield client
     

def test_is_running(client):
    response = client.get('/')
    
    assert "FAIL" in response.data
    
