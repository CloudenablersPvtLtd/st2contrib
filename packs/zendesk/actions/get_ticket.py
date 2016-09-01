from lib.base import BaseZendeskAction
from lib.formatters import get_ticket_result

__all__ = [
    'GetZendeskTicket'
]


class GetZendeskTicket(BaseZendeskAction):
    def run(self, ticket_id):
        ticket = self._client.tickets(id=ticket_id)
        result = get_ticket_result(self._client, ticket)
        return result
