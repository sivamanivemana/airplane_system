# Copyright (c) 2024, sivamani and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns(filters)
    conditions = get_conditions(filters)
    data = get_data(conditions)
    chart = get_chart(data)
    return columns, data, None, chart


def get_columns(filters):
    columns = [
        {
            "fieldname": "airport",
            "fieldtype": "Link",
            "label": "Airport",
            "options": "Airport"
        },
        {
            "fieldname": "status",
            "fieldtype": "Select",
            "label": "Status",
            "options": "Available/Taken",
            "width": 150
        },
        {
            "fieldname": "count",
            "fieldtype": "Int",
            "label": "Count",
            "width": 150
        }
    ]
    return columns


def get_data(conditions):
    query = frappe.db.sql(
        f"""SELECT airport, status, COUNT(status) AS count
            FROM `tabShop`
            WHERE status IS NOT NULL {conditions}
            GROUP BY airport, status""",
        as_dict=True
    )
    return query


def get_conditions(filters):
    conditions = []

    if filters.get("airport"):
        conditions.append(f"airport = '{filters.get('airport')}'")
    if filters.get("status"):
        conditions.append(f"status = '{filters.get('status')}'")

    if conditions:
        return " AND " + " AND ".join(conditions)
    else:
        return ""


def get_chart(data):
    airports = list(set(d["airport"] for d in data))
    available_counts = [d["count"] for d in data if d["status"] == "Available"]
    taken_counts = [d["count"] for d in data if d["status"] == "Taken"]

    chart = {
        "data": {
            "labels": airports,
            "datasets": [
                {
                    "name": "Available",
                    "values": available_counts,
                },
                {
                    "name": "Taken",
                    "values": taken_counts,
                }
            ]
        },
        "type": "bar",
    }
    return chart


def get_report_summary(data):
    total_count = sum(d.get('count', 0) for d in data)
    report_summary = {
        "value": total_count,
        "label": _("Total Count"),
        "datatype": "Int",
        "indicator": "Green" if total_count > 0 else "Red",
    }
    return report_summary
