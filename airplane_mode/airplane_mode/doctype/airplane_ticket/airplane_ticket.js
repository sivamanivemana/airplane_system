// Copyright (c) 2024, Mohan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
            frm.add_custom_button('Assign Seat',() => { 
                let d = new frappe.ui.Dialog({
                    title: 'Assign Seat Number',
                    fields: [
                        {
                            label: 'Seat',
                            fieldname: 'seat',
                            fieldtype: 'Data'
                        },
                    ],
                    size: 'small', // small, large, extra-large 
                    primary_action_label: 'Assign',
                    primary_action(values) {
                        frm.set_value('seat', values['seat']);
                        d.hide();
                        frm.save();
                    }
                });
                
                d.show();
            }, 'Action')
        },
        flight: function(frm) {
            frappe.call({
                method: "airplane_mode.airplane_mode.doctype.airplane_ticket.airplane_ticket.ticket_validations", 
                args : {
                    flight : frm.doc.flight
                },
            })

        }
});
