



function get_fieldOptions(currentValue) {	

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
	


}


function updateTextBox(currentValue) {	

	idNum = currentValue.id.split("-")[1];
	$("#id_chartseries_set-" + idNum + "-field").val($("#id_chartseries_set-" + idNum + "-fieldSelect").val());

}


function getChart(chartId, position) {	

	$.ajax({  
		type: 'GET',  
		url: '/MSQCdb/chartView/' + chartId + '/' + position + '?header=False',  
		dataType: 'html',  
		success: function(htmlStr){
			$("#chart_preview-" + position).html(htmlStr);
			
		} 
	})
}



function getReport(reportId) {	
	$.ajax({  
		type: 'GET',  
		url: '/MSQCdb/reportView/' + reportId + '?header=False',  
		dataType: 'html',  
		success: function(htmlStr){     
			$("#report_preview").html($("#report_preview").html() + htmlStr);
			
		} 
	})
	
}
