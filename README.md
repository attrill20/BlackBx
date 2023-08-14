# FizzBuzz React App

Tech Test for BlckBx from James Attrill
This is a simple React app that fetches and displays FizzBuzz results from a FastAPI server. 

## Getting Started

### Prerequisites

- Node.js and npm (Node Package Manager)
- Python 3
- FastAPI (installed via pip)
- uvicorn (installed via pip)

### Installation

1. Clone this repository to your local machine.

2. Navigate to the project directory - 'cd fizzbuzz-react-app'

3. Install the required dependencies - 'npm install' and 'pip install fastapi uvicorn'

### Running the App

1. Start the FastAPI server to provide the FizzBuzz API - 'uvicorn app:app --host 0.0.0.0 --port 8000'

2. In a separate terminal, start the React app - 'npm start'

### Usage

1. The React app should open in your default web browser at - 'http://localhost:3000'

2. The app will display a list of FizzBuzz results on the web page. Multiples of 3 are labeled as "Fizz," multiples of 5 are labeled as "Buzz," and multiples of both 3 and 5 are labeled as "FizzBuzz."

### Testing

1. In the root folder, run the test package in the terminal using - 'python test.py'
