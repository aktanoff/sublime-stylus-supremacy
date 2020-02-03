"use strict";
const getStdin = require("get-stdin");
const stylusSupremacy = require("stylus-supremacy");

(async () => {
	const data = await getStdin();
    process.stdout.write(process.argv[2]);
    return
  const formattingOptions = JSON.parse(process.argv[2]);

	try {
		process.stdout.write(stylusSupremacy.format(data, formattingOptions));
	} catch (err) {
		throw err;
	}
})();
