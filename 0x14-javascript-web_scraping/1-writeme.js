#!/usr/bin/node
// script that writes to afile using fs

const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];

fs.writeFile(file, data, (err) => {
  if (err) {
    console.error(err);
  }
});
