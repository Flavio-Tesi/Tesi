function myFunction() {
	$.ajax({url: "test.html",
		success:
			function(result) {
				$("#contenuti").html(result).hide().slideDown();
				console.log("Caricato");
			}	
	});
}


$(document).ready(function() {
    $("#tabs").tabs();
	$("#sergio").click(function() {
		console.log("Ci sono");
		myFunction();
	});
});


