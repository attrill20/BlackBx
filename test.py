from urllib import request
import json

# Define the base URL of the FastAPI server
base_url = 'http://127.0.0.1:8000'

# Function to test the /fizzbuzz endpoint


def test_fizzbuzz_endpoint():
    # Use urllib to make a GET request to the /fizzbuzz endpoint
    with request.urlopen(f'{base_url}/fizzbuzz') as response:
        # Read the response data and decode it from bytes to utf-8
        data = response.read().decode('utf-8')
        # Parse the JSON data into a Python dictionary
        result = json.loads(data)

        # Perform tests on the response data
        assert response.status == 200  # Check if the response status is 200 OK
        # Check if the response contains 100 items
        assert len(result) == 100

        # Loop through the results and perform specific checks for FizzBuzz logic
        for i, value in enumerate(result, start=1):
            if i % 3 == 0 and i % 5 == 0:
                assert value == "FizzBuzz"
            elif i % 3 == 0:
                assert value == "Fizz"
            elif i % 5 == 0:
                assert value == "Buzz"
            else:
                assert value == i

        print("FizzBuzz endpoint test passed!")


# Run the test function if this script is executed directly
if __name__ == '__main__':
    test_fizzbuzz_endpoint()
