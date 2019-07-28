"use strict";
const getStdin = require("get-stdin");
const stylusSupremacy = require("stylus-supremacy");

(async () => {
	const data = await getStdin();

	try {
		process.stdout.write(stylusSupremacy.format(data));
	} catch (err) {
		throw err;
	}
})();
