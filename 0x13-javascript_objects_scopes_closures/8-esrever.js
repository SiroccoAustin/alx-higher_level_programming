#!/usr/bin/node

exports.esrever = function (list){
	let reverseArray = [];
	for (let i = list.length; i >= 0; i--){
		reverseArray.push(list[i]);
	}
	return reverseArray;
};
