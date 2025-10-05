#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2]; // first argument → movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, response, body) => {
	  if (err) {
		      console.log(err);
		    } else {
			        const data = JSON.parse(body);
			        console.log(data.title);
			      }
});
