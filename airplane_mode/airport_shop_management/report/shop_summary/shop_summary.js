// Copyright (c) 2024, Mohan and contributors
// For license information, please see license.txt

frappe.query_reports["Shop Summary"] = {
	"filters": [
		{
			"fieldname": "airport",
			"label": __("Airport"),
			"fieldtype": "Link",
			"options": "Airport"
		},
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": ["", "Available", "Occupied"]
		},
	],
	// formatter: (value, row, column, data, default_formatter) => {
	// 	value = default_formatter(value, row, column, data);
	// 	if (column.fieldname === "status" && data.status && data.status == "Available") {
	// 		value = `<div style="color:green">${value}</div>`;
	// 	}
	// 	else if (column.fieldname === "report_status" && data.status && data.status == "Occupied") {
	// 		value = `<div style="color:grey">${value}</div>`;
	// 	}
	// 	return value;
	// },
};
