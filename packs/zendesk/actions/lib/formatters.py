from bunch import bunchify

__all__ = [
    'to_dict',
    'to_object',
    'append_extra_fields',
    'get_ticket_result'
]


def to_dict(object_to_convert):
    return object_to_convert.__dict__


def to_object(dictionary):
    return bunchify(dictionary)


def append_extra_fields(zendesk_obj, extra_fields):
    for key, value in extra_fields.items():
        zendesk_obj.key = lambda: None
        setattr(zendesk_obj, key, value)
    return zendesk_obj


def get_ticket_result(client, ticket):

    ticket_obj = client.tickets(id=ticket.id)
    result = dict(id=ticket.id, subject=ticket.subject,
                  description=ticket.description, url=ticket.url,
                  raw_subject=ticket.raw_subject, status=ticket.status,
                  priority=ticket.priority, type=ticket.type,
                  recipient=ticket.recipient, created_at=ticket.created_at,
                  updated_at=ticket.updated_at)

    if ticket.submitter:
        result['submitter'] = ticket.submitter.name
    elif ticket.submitter_id:
        if ticket_obj.submitter:
            result['submitter'] = ticket_obj.submitter.name

    if ticket.assignee:
        result['assignee'] = ticket.assignee.name
    elif ticket.assignee_id:
        if ticket_obj.assignee:
            result['assignee'] = ticket_obj.assignee.name

    if ticket.organization:
        result['organization'] = ticket_obj.organization.name
    elif ticket.organization_id:
        if ticket_obj.organization:
            result['submitter'] = ticket_obj.organization.name

    if ticket.due_at:
        result['due_at'] = ticket.due_at

    if ticket.tags:
        result['tags'] = ticket.tags
    return result


def get_userid(client, username, email):
    """ user is unique by username and email """
    search_result = client.search(type='user', name=username, email=email)
    user_id = int()
    for user in search_result:
        user_id = user.id
    return user_id


def get_organizationid(client, organization_name):
    """ organization name is unique """
    search_result = client.search(type='organization', name=organization_name)
    organization_id = int()
    for organization in search_result:
        organization_id = organization.id
    return organization_id
