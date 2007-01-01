function myFunction() {
	$.ajax({url: "test.html",
		success:
			function(result) {
				$("#contenuti").html(result).hide().slideDown();
				console.log("Caricato");
			}	
	});
}

function query() {
	console.log("Ciao");
		
	$.ajax({
		url: "/execute",
		type: "get",
		data: {
			cmd: "read_users"
		},
		success: function(data) {
			obj = jQuery.parseJSON(data);
			testo="<table class='basic'>";
			testo+="<th>";
			testo+="Id";
			testo+="</th>";
			testo+="<th>";
			testo+="Nome";
			testo+="</th>";
			testo+="<th>";
			testo+="Codice";
			testo+="</th>";
			testo+="</tr>";

			for (x in obj) {
				testo+="<tr>";
				testo+="<td nowrap valign='top'>";
				testo+=obj[x][0];
				testo+="</td>";
				testo+="<td>";
				testo+=obj[x][1];
				testo+="</td>";
				testo+="<td>";
				testo+=obj[x][2];
				testo+="</td>";
				testo+="</tr>";
			}

			
			testo+="</table>";
			$("#tab").html(testo).hide().slideDown();
		}
	});
}	
	


$(document).ready(function() {
    $("#tabs").tabs();
	$("#users_button").click(function(){
		query();
	});
});


