from fastapi import FastAPI

app = FastAPI()

def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

@app.get('/fizzbuzz')
def get_fizzbuzz_list():
    result = [fizz_buzz(n) for n in range(1, 101)]
    return result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
