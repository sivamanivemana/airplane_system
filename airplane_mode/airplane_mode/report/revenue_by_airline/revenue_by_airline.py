# Copyright (c) 2024, Mohan and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns, data = [
        {
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 230,
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 230,
        },
    ], []

    data = frappe.db.sql("""
    SELECT
        tal.name AS airline,
        COALESCE(SUM(tat.total_amount), 0) AS revenue
    FROM
        `tabAirplane Ticket` tat
    RIGHT JOIN
        `tabAirplane Flight` taf ON tat.flight = taf.name
    RIGHT JOIN
        `tabAirplane` tap ON taf.airplane = tap.name
    RIGHT JOIN
        `tabAirline` tal ON tap.airline = tal.name
    GROUP BY
        tal.name
        """, as_dict=True)
    total_revenue = 0
    for revenue in data:
        total_revenue += revenue.get('revenue')
    chart = {
        "data": {
            "labels": [d.airline for d in data],
            "datasets": [{
                "name": "Revenue by Month",
                "values": [d.revenue for d in data],
            }]
        },
        "type": "donut",
    }

    report_summary = {
        "value": total_revenue,
        "label": _("Total Revenue"),
        "datatype": "Currency",
        "indicator": "Green" if total_revenue > 0 else "Red",
        "currency": "INR",
    }

    return columns, data, None, chart, report_summary
