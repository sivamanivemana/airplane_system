# Copyright (c) 2024, Mohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BookShop(Document):
    def before_insert(self):
        frappe.db.set_value("Shop", self.shop, "status", "Booked")

        # Create a new Tenant document
        tenant_doc = frappe.get_doc({
            "doctype": "Tenant",
            "tenant_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
        })
        tenant_doc.insert()
        frappe.enqueue(
            update_reference, doc=tenant_doc, queue="long", enqueue_after_commit=True
        )


def update_reference(doc):
    try:
        if doc.shop:
            frappe.db.set_value("Shop", doc.shop, "booked_reference", doc.name)
        frappe.db.set_value("Tenant", doc.name, "booked_reference", doc.name)
    except Exception as e:
        frappe.log_error(
            f"An error occurred while updating book reference {doc.name}: {str(e)}")
