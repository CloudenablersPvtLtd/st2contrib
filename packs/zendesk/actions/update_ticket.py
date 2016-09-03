import json
from lib.base import BaseZendeskAction
from lib.formatters import append_extra_fields
from lib.formatters import get_ticket_result
from zenpy.lib import api_objects

__all__ = [
    'UpdateZendeskTicket'
]


class UpdateZendeskTicket(BaseZendeskAction):
    def run(self, ticket_id, comment=None, comment_publicly=None,
            assignee_id=None, status=None, ticket_type=None,
            extra_fields=None):

        ticket_obj = api_objects.Ticket(id=ticket_id)

        if not extra_fields:
            extra_fields = dict()

        if assignee_id:
            extra_fields['assignee_id'] = assignee_id

        if status:
            extra_fields['status'] = status

        if ticket_type:
            extra_fields['type'] = ticket_type

        ticket_obj = append_extra_fields(ticket_obj, extra_fields)

        if comment:
            if comment_publicly.lower() == 'false':
                comment_visibilty = False
            else:
                comment_visibilty = True
            ticket_obj.comment = api_objects.Comment(body=comment,
                                                     public=comment_visibilty)

        update_ticket = self._client.tickets.update(ticket_obj)
        ticket = json.loads(update_ticket._content)['ticket']
        res_ticket_obj = api_objects.Ticket()
        res_ticket_obj = append_extra_fields(res_ticket_obj, ticket)
        result = get_ticket_result(self._client, res_ticket_obj)
        return result
