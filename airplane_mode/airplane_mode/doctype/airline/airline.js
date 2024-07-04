// Copyright (c) 2024, sivamani and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
		if (frm.doc.website){
			cur_frm.add_web_link(frm.doc.website, "Visit Website")
        }
	},
});
