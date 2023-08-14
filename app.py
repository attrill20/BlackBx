from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# // to run server - uvicorn app:app --host 0.0.0.0 --port 8000


app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



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
    result = [str(fizz_buzz(n)) for n in range(1, 101)]
    return result


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
