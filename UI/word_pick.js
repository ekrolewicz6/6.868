var count = 0;


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

function updateRank(word, rank) {
	var http = new XMLHTTPObject();

	// var word = document.getElementById("word").value;
	// var rank = document.getElementById("rank").value;
	
	var params = "word=" + word + "&rank=" + rank;

	http.open("POST", "word_rank.php", true);

	http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	http.setRequestHeader("Content-length", params.length);
	// http.setRequestHeader("Connection", "close");

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
	params = "";

	http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	// http.setRequestHeader("Connection", "close");

	http.onreadystatechange = function() {
		if(http.readyState == 4) {
			if(http.status == 200) {
				var result = http.responseText;
				alert(result);
				// var response_object = eval("(" + result + ")");
				// alert(response_object);
				return result;
				//response object should have the word
			}
		}
	}
	http.send(params);
	return false;
}

$(function() {
	$("#rank").text(count);

	$("#happy").click(function() {
		updateRank($("#word").text(), 1);
		update_count();
		update_word();
	});
	
	$("#sad").click(function() {
		updateRank($("#word").text(), -1);
		update_count();
		update_word();
	});
	
	function update_count() {
		count++;
		$("#rank").text(count);
	}
	
	function update_word() {
		$("#word").text(getWord()); //--> for the new word
		//$("#pos").text(); --> for the part of speech
	}

	$("#word").text(getWord());
	
});


