#!/usr/bin/node
// fetches all the characters in a movie

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) return console.error(error);
  else {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    characters.forEach((characterUrl) => {
      request.get(characterUrl, (chErr, chRes, chBo) => {
        if (chErr) return console.error(error);
        else {
          const character = JSON.parse(chBo);
          console.log(character.name);
        }
      });
    });
  }
});
