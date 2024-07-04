// Copyright (c) 2024, sivamani and contributors
// For license information, please see license.txt

frappe.ui.form.on("Book Shop", {
	refresh:function(frm){
        frm.set_query("shop", function(frm) {
			return {
					filters:{
						"status": "Available"
					},
				};
		});

    }
});
