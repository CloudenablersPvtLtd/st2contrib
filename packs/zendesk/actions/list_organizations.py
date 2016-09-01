from lib.base import BaseZendeskAction
from lib.definitions import RESOURCE_MAP

__all__ = [
    'ListZendeskOrganizations'
]


class ListZendeskOrganizations(BaseZendeskAction):
    def run(self):
        organizations_response = self._client.organizations()
        all_organizations = organizations_response._json[
            RESOURCE_MAP.ORGANIZATIONS]
        result = dict(organizations=all_organizations)
        return result
