#!/usr/bin/node
// displays the satus of a get request

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
