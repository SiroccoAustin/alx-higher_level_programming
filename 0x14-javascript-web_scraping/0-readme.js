#!/usr/bin/node

const myFile = process.argv[2]
const fs = require('fs')

fs.readFile(myFile, "utf8", (error, data) =>{
	if (error){
		console.error(error)
	}
	console.log(data)

});
