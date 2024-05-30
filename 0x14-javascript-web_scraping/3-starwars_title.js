#!/usr/bin/node
// script prints title of star wars movie with episode number

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const moviedata = JSON.parse(body);
  console.log(moviedata.title);
});
