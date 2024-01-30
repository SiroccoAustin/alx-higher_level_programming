#!/usr/bin/node
const filePath = process.argv[2];
const data = process.argv[3];
const fs = require("fs");

fs.writeFile(filePath, data, "utf8", (error) =>{
	if (error){
		console.error(error);
	}
});
