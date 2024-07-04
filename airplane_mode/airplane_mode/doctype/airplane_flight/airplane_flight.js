// Copyright (c) 2024, sivamani and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
    refresh(frm) {
        frm.add_custom_button('Change GateNo', () => {
            let d = new frappe.ui.Dialog({
                title: 'Change Gate Number',
                fields: [
                    {
                        label: 'Gate No',
                        fieldname: 'gate_no',
                        fieldtype: 'Int'
                    },
                ],
                size: 'small', // small, large, extra-large 
                primary_action_label: 'change',
                primary_action(values) {
                    frm.call({
                        method: "change_gate_no",
                        args: {doc:frm.doc, new_gate_no: values['gate_no']}
                    }).then((r) => {
                        frm.set_value('gate_number', values['gate_no']);
                    });
                    d.hide();
                    frm.save();
                }
            });

            d.show();
        }, 'Action')
    },
});
