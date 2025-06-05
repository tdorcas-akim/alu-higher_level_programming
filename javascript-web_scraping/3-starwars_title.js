#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (error, response, body) => {
  if (!error) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.log(error);
  }
});
