function parseMap(dexMap){
	let newMap = {}
	let value = ""
	let pyVal = ""

	pyVal += ("{");
	for (var i in BattleMovedex) {
		pyVal += ("\t\"" + i + "\": {");
		for (var n in BattleMovedex[i]){
			if (typeof(BattleMovedex[i][n]) == "object") {
				value = "{";
				for (var v in BattleMovedex[i][n]){
					value += "'" + String(v) + "': 1, ";
				}
				value += "}"
			}
			else { value = String(BattleMovedex[i][n]) }
			if(String(BattleMovedex[i][n]).indexOf("function") !== -1) { pyVal += ("\t\t\"" + String(n) + "\": \"\"\"" + value + "\"\"\","); }
			else { pyVal += ("\t\t\"" + String(n) + "\": \"" + String(value) + "\","); }
		}
		pyVal += ("\t},")
	}
	pyVal += ("}")
	console.log(pyVal)
}