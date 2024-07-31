#!/usr/bin/node
// prints out the title of a starwars movie
const movieId = process.argv[2];
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
