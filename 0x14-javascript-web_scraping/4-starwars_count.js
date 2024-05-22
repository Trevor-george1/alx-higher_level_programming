#!/usr/bin/node
// Script that prints number of movies where Wedge Antilles is present

const request = require('request');

const apiurl = process.argv[2];

request(apiurl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const results = JSON.parse(body).results;

  const movieswithwedge = results.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1 // if found
      : count; //
  }, 0);
  console.log(movieswithwedge);
});
