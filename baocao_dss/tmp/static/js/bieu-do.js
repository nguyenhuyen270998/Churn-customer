google.charts.setOnLoadCallback(drawChartPbxs);
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChartPbxs() {
	// Tạo data table
	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Users');
	data.addColumn('number', 'Total');
	data.addRows([
	
	]);

	// Set option của biểu đồ
	var options = {
	'title': 'Thống kê số lượng khách hàng theo xác suất dự báo',
	'width': 600,
    'height': 450,
    is3D: true
	};

	// Vẽ biểu đồ từ data và option đã khai báo
	var chart = new google.visualization.PieChart(document.getElementById('chart-pbxs'));
	chart.draw(data, options);
}