from lib.base import BaseZendeskAction
from lib.definitions import RESOURCE_MAP

__all__ = [
    'ListZendeskUsers'
]


class ListZendeskUsers(BaseZendeskAction):
    def run(self):
        users_response = self._client.users()
        all_users = users_response._json[RESOURCE_MAP.USERS]
        result = dict(users=all_users)
        return result
