#!/usr/bin/node
// prints the number of movies where the character "wedge Antiles is present
const api = process.argv[2];
let wedgeCount = 0;
const request = require('request');

request.get(api, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  const movie = JSON.parse(body);
  movie.results.forEach((movie) => {
    movie.character.forEach((character) => {
      if (character.includes('18')) {
        wedgeCount += 1;
      }
    });
  });
  console.log(wedgeCount);
});
