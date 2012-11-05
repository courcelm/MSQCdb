
function get_fieldOptions(value) {	
(function($) {
	idNum = value.id.split("-")[1];
	value = value.options[value.selectedIndex].value;
	
	
	$.ajax({  
		type: 'GET',  
		url: '/MSQCdb/fieldOptions/' + value,  
		dataType: 'html',  
		success: function(html){     
			$("#id_chartseries_set-" + idNum + "-field").html(html);
			$("#id_chartseries_set-" + idNum + "-field").removeAttr('disabled'); 
		} 
	})
	


})(grp.jQuery);
}


