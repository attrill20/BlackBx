from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI instance
app = FastAPI()

# Define the allowed origins for CORS (Cross-Origin Resource Sharing)
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a function for FizzBuzz logic


def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

# Define a route to generate and return a FizzBuzz list


@app.get('/fizzbuzz')
def get_fizzbuzz_list():
    # Generate FizzBuzz results for numbers 1 to 100
    result = [fizz_buzz(n) for n in range(1, 101)]
    return result


# Start the FastAPI application if this script is executed directly
if __name__ == '__main__':
    import uvicorn
    # Run the FastAPI app with host and port settings
    uvicorn.run(app, host='127.0.0.1', port=8000)
