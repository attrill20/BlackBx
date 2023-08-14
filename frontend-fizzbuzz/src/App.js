import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/fizzbuzz');
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
    fetchData();
  }, []);

  return (
    <div className="app">
      <h1>FizzBuzz Results</h1>
      <h2>Here are the results: multiples of 3 = Fizz, multiple of 5 = Buzz, multiples of both = FizzBuzz</h2>
      <ul>
        {data.map((item, index) => (
          <li key={index} className={item}>
            {item}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
