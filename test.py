from urllib import request
import json

base_url = 'http://127.0.0.1:8000'

def test_fizzbuzz_endpoint():
    with request.urlopen(f'{base_url}/fizzbuzz') as response:
        data = response.read().decode('utf-8')
        result = json.loads(data)
        
        assert response.status == 200
        assert len(result) == 100
        
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

if __name__ == '__main__':
    test_fizzbuzz_endpoint()
