#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0
request.get(url, (error, response, body) => {
	if (error){
		console.error(error);
	}
	todos = JSON.parse(body);
	const completed = {};
	for (const i in todos){
		const task = todos[i];
		if (task.completed === true){
			if (completed[task.userId] === undefined){
				count = 1
				completed[task.userId] = count;
			}else{
				count++;
				completed[task.userId] = count;
			}
		}
	}
	console.log(completed);
});
