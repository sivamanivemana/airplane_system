# Copyright (c) 2024, Mohan and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime
from dateutil.relativedelta import relativedelta
from frappe.model.document import Document


class TenantContract(Document):
    def before_save(self):
        get_due_date(self.payment_due_date_of_every_month)

    def on_submit(self):
        frappe.db.set_value("Shop", self.shop, "status", "Occupied")

    def validate(self):
        shop_status = frappe.db.get_value("Shop", self.shop, "status")
        if shop_status == "Occupied":
            frappe.throw("Shop was already occupied.")


@frappe.whitelist()
def get_due_date(payment_due_day):
    today = datetime.today()

    year = today.year
    month = today.month

    try:
        due_date = datetime(year, month+1, int(payment_due_day))
    except ValueError:
        due_date = datetime(year, month, 1) + relativedelta(months=1, days=-1)

    return str(due_date)


@frappe.whitelist()
def set_shop(tenant):
    tenant_doc = frappe.get_doc("Tenant", tenant)
    shop = frappe.db.get_value(
        "Book Shop", {"full_name": tenant_doc.name}, "shop")

    return shop
