import frappe

@frappe.whitelist()
def send_rent_reminder_emails():
    tenants = frappe.db.sql("""SELECT * FROM `tabTenant Contract`""", as_dict=True)
    for tenant in tenants:
        tenant_doc = frappe.get_doc("Tenant", tenant.tenant)
        send_rent_reminder_email(tenant_doc.tenant_name, tenant_doc.email, tenant.payment_due_date)

def send_rent_reminder_email(user_name, email, due_date):
    subject = "Monthly Rent Due Reminder"
    message = f"""<p>Dear {user_name},</p>
                <p>This is a reminder that your rent is due on {due_date}. Please make the payment by the end of the month to avoid any late fees.</p>
                <p>Thank you.</p>"""
    recipients = email
    frappe.sendmail(recipients=recipients, subject=subject, message=message)
