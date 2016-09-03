from zenpy.lib import api_objects
from lib.base import BaseZendeskAction
from lib.formatters import get_ticket_result
from lib.formatters import append_extra_fields
from lib.definitions import RESOURCE_MAP

__all__ = [
    'ListZendeskTickets'
]


class ListZendeskTickets(BaseZendeskAction):
    def run(self):
        tickets_response = self._client.tickets()
        all_tickets = tickets_response._json[RESOURCE_MAP.TICKETS]
        result = dict(tickets=list())

        for ticket in all_tickets:
            ticket_obj = api_objects.Ticket()
            ticket_obj = append_extra_fields(ticket_obj, ticket)
            result['tickets'].append(
                get_ticket_result(self._client, ticket_obj))

        return result
