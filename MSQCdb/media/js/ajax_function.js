



function get_fieldOptions(currentValue) {	
(function($) {
	idNum = currentValue.id.split("-")[1];
	value = currentValue.options[currentValue.selectedIndex].value;
	text= currentValue.options[currentValue.selectedIndex].text;
	
	$("#id_chartseries_set-" + idNum + "-field").val('');
	$("#id_chartseries_set-" + idNum + "-fieldSelect").remove();
	$("#id_chartseries_set-" + idNum + "-field")
    .after('<select style="width: 0px;" id="id_chartseries_set-' + idNum + '-fieldSelect" name="chartseries_set-' + idNum + '-fieldSelect" onchange="updateTextBox(this);">' +
          '</select>');
	
	
	$.ajax({  
		type: 'GET',  
		url: '/MSQCdb/fieldOptions/' + value,  
		dataType: 'html',  
		success: function(html){     
			$("#id_chartseries_set-" + idNum + "-fieldSelect").html(html);
			
		},
		error: function(XMLHttpRequest, textStatus, errorThrown)
		{
			registerError(textStatus);
		}
	})
	

})(grp.jQuery);
}


function updateTextBox(currentValue) {	
(function($) {
	idNum = currentValue.id.split("-")[1];
	$("#id_chartseries_set-" + idNum + "-field").val($("#id_chartseries_set-" + idNum + "-fieldSelect").val());
})(grp.jQuery);
}


function getChart(chartId) {	
(function($) {
	
	$.ajax({  
		type: 'GET',  
		url: '/MSQCdb/chartView/' + chartId,  
		dataType: 'html',  
		success: function(html){     
			$("#chart_preview").html(html);
			
		} 
	})
	

})(grp.jQuery);
}

