frappe.listview_settings['Shop'] = {
    get_indicator: function(doc) {
        if (doc.status === "Booked") {
            return [__("Booked"), "orange", "status,=,Booked"];
        } else if (doc.status === "Taken") {
            return [__("Taken"), "grey", "status,=,Taken"];
        } else {
            return [__("Available"), "green"];
        }
    }
};