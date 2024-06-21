frappe.ready(function() {
	// bind events here
	var urlParams = new URLSearchParams(window.location.search);
    var flight = urlParams.get('flight');
    var flightPrice = urlParams.get('flight_price');

    // Set the values in the form fields
    if (flight) {
        $('[data-fieldname="flight"]').val(flight).prop('readonly', true);
    }
    if (flightPrice) {
        $('[data-fieldname="flight_price"]').val(flightPrice).prop('readonly', true);
    }
})