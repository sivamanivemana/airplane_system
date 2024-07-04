# Copyright (c) 2024, sivamani and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from dateutil.relativedelta import relativedelta


class RentPayment(Document):
    def on_submit(self):
        if self.payment_due_date:
            next_payment_due_date = get_first_date_of_next_month(
                self.payment_due_date)
            frappe.db.set_value("Tenant Contract", self.tenant,
                                "payment_due_date", next_payment_due_date)


def get_first_date_of_next_month(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d')

    first_of_next_month = (date_obj.replace(
        day=1) + relativedelta(months=1)).strftime('%Y-%m-%d')

    return first_of_next_month
