function parseObj(object, lvl) {
	let newMap = {}
	let value = "{\n"
	let n = 0
	let tabs = ""
	n = 0
	
	while ( n <= lvl)
	{
		tabs += "\t"
		n += 1
	}

    var size = 0, key;
    for (key in object) {
        if (object.hasOwnProperty(key)) size++;
    }
    if (size === 0) { return "{}," ; }
	for (var i in object) {
		if(typeof(object[i]) == "object") {
			value += "\n" + tabs + "\""  + "" + i + "\": " + parseObj(object[i], lvl + 1)
		}
		else if (typeof(dexMap[i][n]) == "boolean") {
			if (dexMap[i][n] == false) { value = "False"; }
			else { value = "True"; }
			pyVal += ("\t\t\"" + String(n) + "\": "  + String(value) + ",\n");
		}
		else if (typeof(dexMap[i][n]) == "number") {
			value = String(dexMap[i][n])
			pyVal += ("\t\t\"" + String(n) + "\": "  + String(value) + ",\n");
		}
		else
		{
			if(String(object[i]).indexOf("function") !== -1) { value += ("\t\t\"" + String(n) + "\": \"\"\"" + object[i] + "\"\"\",\n"); }
			else { value += tabs + "\"" + i + "\": \"" + object[i] + "\",\n"; }
		}
	}
	n = 0
	while ( n < lvl)
	{
		value += "\t"
		n += 1
	}
	value += "},"
	return value
}

function parseMap(dexMap){
	let newMap = {}
	let value = ""
	let pyVal = ""

	pyVal += ("{");
	for (var i in dexMap) {
		pyVal += ("\t\"" + i + "\": {\n");
		for (var n in dexMap[i]){
			if (typeof(dexMap[i][n]) == "object") {
				value = parseObj(dexMap[i][n], 2);
				pyVal += ("\t\t\"" + String(n) + "\": "  + String(value) + "\n");
			}
			else if (typeof(dexMap[i][n]) == "boolean") {
				if (dexMap[i][n] == false) { value = "False"; }
				else { value = "True"; }
				pyVal += ("\t\t\"" + String(n) + "\": "  + String(value) + ",\n");
			}
			else if (typeof(dexMap[i][n]) == "number") {
				value = String(dexMap[i][n])
				pyVal += ("\t\t\"" + String(n) + "\": "  + String(value) + ",\n");
			}
			else {
				value = String(dexMap[i][n])
				if(String(dexMap[i][n]).indexOf("function") !== -1) { pyVal += ("\t\t\"" + String(n) + "\": \"\"\"" + value + "\"\"\",\n"); }
				else { pyVal += ("\t\t\"" + String(n) + "\": \""  + String(value) + "\",\n"); }
			}
		}
		pyVal += ("\t},\n")
	}
	pyVal += ("}\n")
	return pyVal
}