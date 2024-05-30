#!/usr/bin/node
// script that fetches data from web page

const request = require('request');
const fs = require('fs');

const apiurl = process.argv[2];
const file = process.argv[3];

request(apiurl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(file, body, 'utf-8', function (error, data) {
    if (error) {
      console.error(error);
    }
  });
});
