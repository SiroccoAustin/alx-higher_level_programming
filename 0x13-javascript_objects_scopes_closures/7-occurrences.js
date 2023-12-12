#!/usr/bin/node

exports.nbOccurences = function (list, searchElement){
	let repetition = 0;

	for (let i = 0; i < list.length; i++){
		if (list[i] === searchElement){
			repetition += 1;
		}
	}
	return repetition;
};
