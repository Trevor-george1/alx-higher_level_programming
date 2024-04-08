#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
if (isNaN(num)) {
  console.log('Missing size');
}
for (let i = 1; i <= num; i++) {
  let row = '';
  for (let j = 1; j <= num; j++) {
    row += 'X';
  }
  console.log(row);
}
