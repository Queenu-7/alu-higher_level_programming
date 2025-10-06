#!/usr/bin/node
const request = require('request');
const fs = require('fs');


const url = process.argv[2]; //first argument url
const filepath = process.argv[3]; // second argument file path

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
	}


  fs.writeFile(filepath, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
	  }
	});
