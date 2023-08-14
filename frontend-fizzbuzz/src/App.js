import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
	// State to hold the fetched FizzBuzz data
	const [data, setData] = useState([]);

	// useEffect to fetch data when the component mounts
	useEffect(() => {
		async function fetchData() {
			try {
				const response = await axios.get("http://127.0.0.1:8000/fizzbuzz");
				setData(response.data);
			} catch (error) {
				console.error("Error fetching data:", error);
			}
		}
		fetchData();
	}, []);

	// returns the content for the site
	return (
		<div className="app">
			<h1>FizzBuzz Results</h1>
			<h2>
				Here are the results: multiples of 3 = Fizz, multiples of 5 = Buzz,
				multiples of both = FizzBuzz
			</h2>
			<ul>
				{/* Map through the data and display each FizzBuzz result */}
				{data.map((item, index) => (
					<li
						key={index}
						className={item}>
						{item}
					</li>
				))}
			</ul>
		</div>
	);
}

export default App;
