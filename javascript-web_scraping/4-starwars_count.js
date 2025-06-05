#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const wedgeId = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    let count = 0;

    for (const film of data.results) {
      if (film.characters.includes(wedgeId)) {
        count++;
      }
    }

    console.log(count);
  } else {
    console.log(error);
  }
});
