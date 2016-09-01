from lib.base import BaseZendeskAction
from lib.definitions import HTTP_CODES
from lib.definitions import RESPONSE_MESSAGES
from zenpy.lib import api_objects

__all__ = [
    'DeleteZendeskTicket'
]


class DeleteZendeskTicket(BaseZendeskAction):
    def run(self, ticket_id):
        ticket_obj = api_objects.Ticket(id=ticket_id)
        result = dict()

        response = self._client.tickets.delete(ticket_obj)
        if response.status_code == HTTP_CODES.SUCCESS or \
                        response.status_code == HTTP_CODES.NO_CONTENT:
            result['status'] = RESPONSE_MESSAGES.SUCCESS
            result['message'] = 'Ticket %s' % RESPONSE_MESSAGES.DELETE_SUCCESS
            result['id'] = ticket_id
        return result

