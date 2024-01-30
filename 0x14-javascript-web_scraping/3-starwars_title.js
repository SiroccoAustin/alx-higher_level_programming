#!/usr/bin/node
const url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];
const request = require("request");
request.get(url, (error, response, body) =>{
	if (error){
		console.error(error);
	}
	const data = JSON.parse(body);
	console.log(data.title);
});
