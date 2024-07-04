frappe.listview_settings['Shop'] = {
    get_indicator: function(doc) {
        if (doc.status === "Booked") {
            return [__("Booked"), "orange", "status,=,Booked"];
        } else if (doc.status === "Occupied") {
            return [__("Occupied"), "grey", "status,=,Occupied"];
        } else {
            return [__("Available"), "green"];
        }
    }
};