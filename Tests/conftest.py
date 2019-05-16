import pytest

@pytest.fixture(scope='session', autouse=True)
def case_request():
     request_data = [
        {
        },
        {
            'user_action': '-1',
            'feedback': 'Bob'
        },
        {
            'user_action': 'null',
            'feedback': 'Bob'
        },
        {
            'user_action': '10',
            'feedback': 'Bob'
        },
        {
            'user_action': '0'
        },
        {
            'user_action': '11'
        },
        {
            'user_action': '7'
        },
        {
            'user_action': '6',
            'feedback': 'Bob'
        },
        {
            'feedback': 'Bob'
        },
    ]
     return request_data

@pytest.fixture(scope='session', autouse=True)
def case_response():
    response_data = [
        {
            "errors": [
                "Invalid rate"
            ],"status": "error"
        },
        {
            "status": "ok"
        },
        {
            "errors": [
                "FeedBack is not required"
            ],
            "status": "error"
        },
        {
            "errors": [
                "FeedBack is required"
            ],
            "status": "error"
        },
        {
            "errors": [
                "Missed required field user_action"
            ],
            "status": "error"
        }
    ]
    return response_data

@pytest.fixture(scope='function')
def case_header():
    header_values = [
        {
            'Content-type': 'application/json'
        },
        {
            'Content-type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
        },
        {
            'Content-type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'
        },
    ]
    return header_values
