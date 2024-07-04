# Copyright (c) 2024, sivamani and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
    def get_doc_before_save(self) -> Document:
        return super().get_doc_before_save()

    def before_save(self):
        if self.first_name and self.last_name:
            self.full_name = self.first_name + " " + self.last_name
        elif self.first_name:
            self.full_name = self.first_name
        elif self.last_name:
            self.full_name = self.last_name
        else:
            self.full_name = self.first_name
