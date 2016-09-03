from lib.base import BaseZendeskAction
from lib.formatters import append_extra_fields
from lib.formatters import get_ticket_result
from zenpy.lib import api_objects

__all__ = [
    'CreateZendeskTicket'
]


class CreateZendeskTicket(BaseZendeskAction):
    def run(self, subject, description, ticket_type, priority=None,
            requester_id=None, extra_fields=None):
        ticket_obj = api_objects.Ticket(subject=subject,
                                        description=description,
                                        type=ticket_type)
        if not extra_fields:
            extra_fields = dict()

        if priority:
            extra_fields['priority'] = priority

        if requester_id:
            extra_fields['requester_id'] = requester_id

        ticket_obj = append_extra_fields(ticket_obj, extra_fields)

        ticket_audit = self._client.tickets.create(ticket_obj)
        result = get_ticket_result(self._client, ticket_audit.ticket)
        return result
