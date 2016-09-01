# ZENDESK integration pack

This pack consists of a sample ZENDESK sensor and a ZENDESK action.

## Configuration

Actions come with a json configuration file (config.yaml). You'll need to configure the following:

* ``email`` - Email of the ZENDESK user (e.g. ``user@company.com``)
* ``subdomain`` - Zendesk User's subdomain.
* ``password`` - Password of the user.
* ``api_token`` - API Token.
* ``oauth_token`` - OAuth Token.

Email and Subdomain fields are mandatory. Any one from password/api_token/oauth_token must be provided.

## Actions

* ``list_tickets`` - Lists all Zendesk tickets.
* ``list_users`` - Lists all Zendesk users.
* ``list_organizations`` - Lists all Zendesk organizations.
* ``get_ticket`` - Retrieves details for a particular ticket.
* ``create_ticket`` - Creates a new Zendesk ticket.
* ``update_ticket`` - Updates a Zendesk ticket.
* ``search_ticket`` - Search and retrieves Zendesk ticket(s) based on the provided parameters.
* ``delete_ticket`` - Deletes a Zendesk ticket.


## ChatOps commands

By default, this pack also includes ChatOps commands (aliases) which allow you
to query your StackStorm installation for things such as available actions,
sensors and more.

* ``!zendesk get ticket <ticket_id>`` - Retrieves details for a particular ticket.
* ``!zendesk create ticket <subject> <description> <type>`` - Creates a new ticket.
* ``!zendesk update ticket <ticket_id> <comment>`` - Updates a ticket.
* ``!zendesk search_by_subject ticket <subject>`` - Search and retrieves tickets by subject.
* ``!zendesk search_by_status ticket <status>`` - Search and retrieves tickets by status.
* ``!zendesk search_by_description ticket <description>`` - Search and retrieves tickets by description.
* ``!zendesk close ticket <ticket_id>`` - Closes a ticket.
* ``!delete zendesk ticket <ticket_id>`` - Deletes a ticket.
* ``!get zendesk ticket <ticket_id>`` - Retrieves details for a particular ticket.
* ``!create zendesk ticket <subject> <description> <type>`` - Creates a new ticket.
* ``!update zendesk ticket <ticket_id> <comment>`` - Updates a ticket.
* ``!search_by_subject zendesk ticket <subject>`` - Search and retrieves tickets by subject.
* ``!search_by_status zendesk ticket <status>`` - Search and retrieves tickets by status.
* ``!search_by_description zendesk ticket <description>`` - Search and retrieves tickets by description.
* ``!close zendesk ticket <ticket_id>`` - Closes a ticket.
* ``!delete zendesk ticket <ticket_id>`` - Deletes a ticket.