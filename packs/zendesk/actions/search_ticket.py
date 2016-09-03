from lib.base import BaseZendeskAction
from lib.definitions import RESOURCE_MAP

__all__ = [
    'SearchZendeskTicket'
]


class SearchZendeskTicket(BaseZendeskAction):
    def run(self, ticket_id=None, requester_id=None, subject=None,
            description=None, ticket_type=None, priority=None,
            assignee_id=None, status=None, extra_search_fields=None):

        search_query = dict()
        result = dict()
        params = dict(ticket_id=ticket_id, requester_id=requester_id,
                      subject=subject, description=description,
                      type=ticket_type, priority=priority,
                      assignee_id=assignee_id, status=status)
        if extra_search_fields:
            params.update(extra_search_fields)

        for key, value in params.items():
            if value:
                search_query[key] = value

        search_result = self._client.search(type='ticket', **search_query)
        result[RESOURCE_MAP.TICKETS] = search_result._json['results']
        return result
