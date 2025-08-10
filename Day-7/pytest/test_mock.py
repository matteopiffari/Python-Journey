import pytest
from mock import *

# In this case we simulate a successful API call without actually hitting the endpoint

def testApiCall(mocker):
    # Mock the requests.get method
    mock_get = mocker.patch('mock.requests.get')
    
    # Set up the mock to return a response with status code 200 and a JSON body
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"key": "value"}
    
    # Call the function that uses requests.get
    result = apiCall("test")

    # Assert that the result is as expected
    assert result == {"key": "value"}
    
    # Assert that requests.get was called with the correct URL
    mock_get.assert_called_once_with("https://localhost/api?param=test")