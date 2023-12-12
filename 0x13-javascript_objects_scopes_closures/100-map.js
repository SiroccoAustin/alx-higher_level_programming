#!/usr/bin/node

const array = require("./100-data.js").list;


console.log(array);
console.log(array.map((el, ind) => el * ind));
