from zenpy import Zenpy

#  from st2actions.runners.pythonrunner import Action
__all__ = [
    'BaseZendeskAction'
]


class Action(object):
    def __init__(self, config):
        self.config = config


class BaseZendeskAction(Action):
    def __init__(self, config):
        super(BaseZendeskAction, self).__init__(config=config)
        if config is None:
            raise ValueError("No connection configuration details found")
        self._client = self._get_client()

    def _get_client(self):
        config = self.config

        if not config['password'] and not config[
            'api_token'] and not config['oauth_token']:
            raise Exception(
                'Password or API Token or OAuth Token should be provided')

        creds = dict(email=config['email'], subdomain=config['subdomain'])

        if config['password']:
            creds['password'] = config['password']
        elif config['api_token']:
            creds['token'] = config['api_token']
        elif config['oauth_token']:
            creds['oauth_token'] = config['oauth_token']

        client = Zenpy(**creds)
        return client