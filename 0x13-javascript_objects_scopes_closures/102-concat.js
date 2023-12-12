#!/usr/bin/node

const fs = require('fs');
let contact = '';

contact = contact.concat(fs.readFileSync(process.argv[2]));
contact = contact.concat(fs.readFileSync(process.argv[3]));
fs.writeFileSync(process.argv[4], contact);
