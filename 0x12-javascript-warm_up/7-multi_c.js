#!/usr/bin/node
const arg = process.argv[2];

const num = parseInt(arg);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
}
for (let i = 1; i <= num; i++) {
  console.log('C is fun');
}
