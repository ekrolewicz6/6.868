
function XMLHTTPObject() {
	var xmlhttp = false;
	//If XMLHTTPReques is available
	if(XMLHttpRequest) {
		try {
			xmlhttp = new XMLHttpRequest();
		} catch(e) {
			xmlhttp = false;
		}
	} else if( typeof ActiveXObject != 'undefined') {
		//Use IE's ActiveX items to load the file.
		try {
			xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
		} catch(e) {
			try {
				xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
			} catch(E) {
				xmlhttp = false;
			}
		}
	} else {
		xmlhttp = false;
		//Browser don't support Ajax
	}
	return xmlhttp;
}

function updateRank() {
	var http = new XMLHTTPObject();

	var word = document.getElementById("word").value;
	var rank = document.getElementById("rank").value;
	
	var params = "word=" + word + "&rank=" + rank;

	http.open("POST", "word_rank.php", true);

	http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	http.setRequestHeader("Content-length", params.length);
	http.setRequestHeader("Connection", "close");

	http.onreadystatechange = function() {
		if(http.readyState == 4) {
			if(http.status == 200) {
				var result = http.responseText;
			}
		}
	}
	http.send(params);
	return false;
}

function getWord() {

	var http = new XMLHTTPObject();

	http.open("POST", "get_word.php", true);

	http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	http.setRequestHeader("Connection", "close");

	http.onreadystatechange = function() {
		if(http.readyState == 4) {
			if(http.status == 200) {
				var result = http.responseText;
				var response_object = eval("(" + result + ")");
				//response object should have the word
			}
		}
	}
	http.send(params);
	return false;
}
