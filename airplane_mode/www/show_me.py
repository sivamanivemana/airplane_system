import frappe


def get_context(context):

    color = frappe.form_dict.get('color', 'red')

    context.color = color
    return context
