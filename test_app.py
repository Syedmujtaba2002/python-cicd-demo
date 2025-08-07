from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert "Hello from Flask CI/CD App and welcome to Elevate labs 🚀This is the webhook process and elevate labs" in response.data.decode('utf-8')

