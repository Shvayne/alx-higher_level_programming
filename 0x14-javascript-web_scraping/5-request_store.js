#!/usr/bin/node
//scraps a webpage

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request.get(url, (error, response, body) => {
	if (error) return console.error(error);
	fs.writeFile(fileName, body, (error) => {
		if (error) return console.error(error);
	});
});
