#!/usr/bin/node
const url = process.argv[2];
const request = require("request");
let count = 0;
const last = "/18/";
request.get(url, (error, response, body) => {
	if (error){
		console.error(error);
	}
	const data = JSON.parse(body).results;
	for (const key of data){
		if (key.hasOwnProperty("characters")){
			//console.log(key.characters);
			for (let i = 0; i < key.characters.length; i++){
				if (key.characters[i].endsWith(last)){
					count++;
				}
			}
		}
	}
	console.log(count);
});
