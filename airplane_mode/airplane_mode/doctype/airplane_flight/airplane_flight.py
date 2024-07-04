# Copyright (c) 2024, Mohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator
import json


class AirplaneFlight(WebsiteGenerator):
    def before_submit(self):
        self.status = 'Completed'


@frappe.whitelist()
def change_gate_no(doc, new_gate_no):
    doc = json.loads(doc)
    new_gate_no = json.loads(new_gate_no)
    all_tickets_related_to_flight = frappe.db.get_all(
        "Airplane Ticket", filters={"flight": doc.get('name')}, fields=["name"])
    if all_tickets_related_to_flight:
        for ticket in all_tickets_related_to_flight:
            frappe.db.set_value("Airplane Ticket", ticket.name,
                                "gate_number", new_gate_no)
