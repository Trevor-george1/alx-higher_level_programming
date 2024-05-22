#!/usr/bin/node
// script displays status code of a GET request

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log('code:', response.statusCode);
});
