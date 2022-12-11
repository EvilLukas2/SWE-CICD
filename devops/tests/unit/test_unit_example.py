from app import generateGreeting

def test_greeting():
    response = generateGreeting("Robin")

    assert 'Hello Robin' in response


