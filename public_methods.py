import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_public_events():
    try:
        events = frappe.get_all(
            'Club Events',
            fields=[
                "club_event_name", 
                "club_name", 
                "event_starting_time", 
                "event_ending_time", 
                "event_venue", 
                "event_status"
            ]
        )
        return events
    except Exception as e:
        frappe.log_error(title="Get Public Events Error", message=frappe.get_traceback())
        return []
