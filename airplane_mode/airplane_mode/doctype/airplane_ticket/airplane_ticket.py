# Copyright (c) 2024, Mohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random


class AirplaneTicket(Document):
    def before_save(self):
        total_amount = 0
        for item in self.add_ons:
            total_amount += item.amount
        self.total_amount = total_amount + self.flight_price

    def validate(self):
        self.remove_duplicate_add_ons()
        self.assign_random_seat()

    def remove_duplicate_add_ons(self):
        unique_add_ons = []
        add_on_items = set()

        for add_on in self.add_ons:
            if add_on.item not in add_on_items:
                add_on_items.add(add_on.item)
                unique_add_ons.append(add_on)

            self.add_ons = unique_add_ons

    def assign_random_seat(self):
        a = ['A', 'B', 'C', 'D', 'E']
        if not self.seat:
            self.seat = f"{random.randint(00,99)}{random.choice(a)}"

    def on_submit(self):
        if self.status != 'Boarded':
            frappe.throw(
                "Please change ticket status to 'Boarded' for ticket submission")


@frappe.whitelist()
def ticket_validations(flight):
    try:
        flight_doc = frappe.get_doc("Airplane Flight", flight)

        airplane_capacity = frappe.db.get_value(
            "Airplane", flight_doc.airplane, "capacity") or 0

        booked_tickets_count = frappe.db.count(
            "Airplane Ticket", filters={"flight": flight})

        if booked_tickets_count >= airplane_capacity:
            frappe.throw("All seats are reserved for this flight.")

    except frappe.DoesNotExistError:
        frappe.throw(f"Flight {flight} does not exist.")

    except Exception as e:
        frappe.throw(f"An error occurred: {str(e)}")
