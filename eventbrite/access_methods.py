# -*- coding: utf-8 -*-
"""
ayy lmao
Last Generated: 2015-01-28 13:03:49.956806
This module (access_methods.py) is autogenerated from the Eventbrite API
documentation. Any and all changes to this module must be implemented as
p art of that autogeneration. Therefore, we cannot accept any pull requests,
as the next generation of this module will the changes to be overwritten.
"""


class AccessMethodsMixin(object):

    def get_categories(self, **data):
        """
        GET /categories/
        Returns a list of :format:`category` as ``categories``, including
        subcategories nested.
        """
        return self.get("/categories/", data=data)

    def get_category(self, id, **data):
        """
        GET /categories/:id/
        Gets a :format:`category` by ID as ``category``.
        """
        return self.get("/categories/{0}/".format(id), data=data)

    def get_subcategories(self, **data):
        """
        GET /subcategories/
        Returns a list of :format:`subcategory` as ``subcategories``.
        """
        return self.get("/subcategories/", data=data)

    def get_subcategory(self, id, **data):
        """
        GET /subcategories/:id/
        Gets a :format:`subcategory` by ID as ``subcategory``.
        """

        return self.get("/subcategories/{0}/".format(id), data=data)

    def get_formats(self, **data):
        """
        GET /format/
        Returns a list of :format:`format` as ``formats``.
        """
        return self.get("/format/", data=data)

    def get_format(self, id, **data):
        """
        GET /format/:id/
        Gets a :format:`format` by ID as ``format``.
        """

        return self.get("/format/{0}/".format(id), data=data)

    def get_event(self, id, **data):
        """
        GET /events/:id/
        Returns an :format:`event` for the specified event.
        """
        return self.get("/events/{0}/".format(id), data=data)

    def get_event_ticket_classes(self, id, **data):
        """
        GET /events/:id/ticket_classes/
        Returns a paginated response with a key of ``ticket_classes``,
        containing a list of :format:`ticket_class`.
        """
        return self.get("/events/{0}/ticket_classes/".format(id), data=data)

    def get_event_ticket_class(self, id, ticket_class_id, **data):
        """
        GET /events/:id/ticket_classes/:ticket_class_id/
        Gets and returns a single :format:`ticket_class` by ID, as the key
        ``ticket_class``.
        """
        return self.get("/events/{0}/ticket_classes/{1}/".format(
            id, ticket_class_id), data=data)

    def get_event_attendees(self, id, **data):
        """
        GET /events/:id/attendees/
        Returns a paginated response with a key of ``attendees``, containing
        a list of :format:`attendee`.
        """
        return self.get("/events/{0}/attendees/".format(id), data=data)

    def get_event_attendee(self, id, attendee_id, **data):
        """
        GET /events/:id/attendees/:attendee_id/
        Returns a single :format:`attendee` by ID, as the key ``attendee``.
        """
        return self.get("/events/{0}/attendees/{1}/".format(
            id, attendee_id), data=data)

    def get_event_orders(self, id, **data):
        """
        GET /events/:id/orders/
        Returns a paginated response with a key of ``orders``, containing a
        list of :format:`order` against this event.
        """

        return self.get("/events/{0}/orders/".format(id), data=data)

    def get_event_discounts(self, id, **data):
        """
        GET /events/:id/discounts/
        Returns a paginated response with a key of ``discounts``,
        containing a list of :format:`discounts <discount>` available on
        this event.
        """

        return self.get("/events/{0}/discounts/".format(id), data=data)

    def post_event_discounts(self, id, **data):
        """
        POST /events/:id/discounts/
        Creates a new discount; returns the result as a :format:`discount`
        as the key ``discount``.
        """

        return self.post("/events/{0}/discounts/".format(id), data=data)

    def get_event_discounts(self, id, discount_id, **data):
        """
        GET /events/:id/discounts/:discount_id/
        Gets a :format:`discount` by ID as the key ``discount``.
        """
        return self.get("/events/{0}/discounts/{1}/".format(id,discount_id), data=data)

    def post_event_discounts(self, id, discount_id, **data):
        """
        POST /events/:id/discounts/:discount_id/
        Updates a discount; returns the result as a :format:`discount` as the
        key ``discount``.
        """
        
        return self.post("/events/{0}/discounts/{1}/".format(id,discount_id), data=data)

    def delete_event_discounts(self, id, discount_id, **data):
        """
        DELETE /events/:id/discounts/:discount_id/
        Deletes a discount.
        """

        return self.delete("/events/{0}/discounts/{1}/".format(
            id, discount_id), data=data)

    def get_event_public_discounts(self, id, **data):
        """
        GET /events/:id/public_discounts/
        Returns a paginated response with a key of ``discounts``,
        containing a list of public :format:`discounts <discount>` available
        on this event. Note that public discounts and discounts have exactly
        the same form and structure; they're just namespaced separately, and
        public ones (and the public GET endpoints) are visible to anyone who
        can see the event.
        """

        return self.get("/events/{0}/public_discounts/".format(id), data=data)

    def post_event_public_discounts(self, id, **data):
        """
        POST /events/:id/public_discounts/
        Creates a new public discount; returns the result as a
        :format:`discount` as the key ``discount``.
        """
        
        return self.post("/events/{0}/public_discounts/".format(id), data=data)

    def get_event_public_discounts(self, id, discount_id, **data):
        """
        GET /events/:id/public_discounts/:discount_id/
        Gets a public :format:`discount` by ID as the key ``discount``.
        """
        
        return self.get("/events/{0}/public_discounts/{1}/".format(id,discount_id), data=data)

    def post_event_public_discounts(self, id, discount_id, **data):
        """
        POST /events/:id/public_discounts/:discount_id/
        Updates a public discount; returns the result as a
        :format:`discount` as the key ``discount``.
        """
        
        return self.post("/events/{0}/public_discounts/{1}/".format(id,discount_id), data=data)

    def delete_event_public_discounts(self, id, discount_id, **data):
        """
        DELETE /events/:id/public_discounts/:discount_id/
        Deletes a public discount.
        """
        
        return self.delete("/events/{0}/public_discounts/{1}/".format(id,discount_id), data=data)

    def get_event_access_codes(self, id, **data):
        """
        GET /events/:id/access_codes/
        Returns a paginated response with a key of ``access_codes``,
        containing a list of :format:`access_codes <access_code>` available
        on this event.
        """
        
        return self.get("/events/{0}/access_codes/".format(id), data=data)

    def post_event_access_codes(self, id, **data):
        """
        POST /events/:id/access_codes/
        Creates a new access code; returns the result as a :format:`access_code` as the
        key ``access_code``.
        """
        
        return self.post("/events/{0}/access_codes/".format(id), data=data)

    def get_event_access_code(self, id, access_code_id, **data):
        """
        GET /events/:id/access_codes/:access_code_id/
        Gets a :format:`access_code` by ID as the key ``access_code``.
        """
        
        return self.get("/events/{0}/access_codes/{1}/".format(id,access_code_id), data=data)

    def post_event_access_code(self, id, access_code_id, **data):
        """
        POST /events/:id/access_codes/:access_code_id/
        Updates an access code; returns the result as a :format:`access_code` as the
        key ``access_code``.
        """
        
        return self.post("/events/{0}/access_codes/{1}/".format(id,access_code_id), data=data)

    def get_event_transfers(self, id, **data):
        """
        GET /events/:id/transfers/
        Returns a list of :format:`transfers` for the event.
        """
        
        return self.get("/events/{0}/transfers/".format(id), data=data)

    def get_media(self, id, **data):
        """
        GET /media/:id/
        Return an :format:`image` for a given id.
        .. _get-media-upload:
        """
        
        return self.get("/media/{0}/".format(id), data=data)

    def get_media_upload(self, **data):
        """
        GET /media/upload/
        See :ref:`media-uploads`.
        .. _post-media-upload:
        """
        return self.get("/media/upload/", data=data)

    def post_media_upload(self, **data):
        """
        POST /media/upload/
        See :ref:`media-uploads`.
        """
        return self.post("/media/upload/", data=data)

    def get_order(self, id, **data):
        """
        GET /orders/:id/
        Gets an :format:`order` by ID as the key ``order``.
        """
        
        return self.get("/orders/{0}/".format(id), data=data)

    def post_organizers(self, **data):
        """
        POST /organizers/
        Makes a new organizer.
        Returns an :format:`organizer` as ``organizer``.
        :param str organizer.name: The name of the organizer.
        :param str description.html: The description of the organizer.
        :param str logo.id: The logo id of the organizer.
        """
        return self.post("/organizers/", data=data)

    def get_organizers(self, id, **data):
        """
        GET /organizers/:id/
        Gets an :format:`organizer` by ID as ``organizer``.
        """
        
        return self.get("/organizers/{0}/".format(id), data=data)

    def post_organizers(self, id, **data):
        """
        POST /organizers/:id/
        Updates an :format:`organizer` and returns it as as ``organizer``.
        """
        
        return self.post("/organizers/{0}/".format(id), data=data)

    def get_system_timezones(self, **data):
        """
        GET /system/timezones/
        Returns a paginated response with a key of ``timezones``,
        containing a list of :format:`timezones <timezone>`.
        """
        return self.get("/system/timezones/", data=data)

    def get_user(self, id, **data):
        """
        GET /users/:id/
        Returns a :format:`user` for the specified user as ``user``. If you want
        to get details about the currently authenticated user, use ``/users/me/``.
        """
        
        return self.get("/users/{0}/".format(id), data=data)

    def get_user_orders(self, id, **data):
        """
        GET /users/:id/orders/
        Returns a paginated response of :format:`orders <order>`, under
        the key ``orders``, of all orders the user has placed (i.e. where the user
        was the person buying the tickets).
        :param int id: The id assigned to a user.
        :param datetime changed_since: (optional) Only return attendees changed on or after the time given.
        .. note:: A datetime represented as a string in ISO8601 combined date and time format, always in UTC.
        """
        
        return self.get("/users/{0}/orders/".format(id), data=data)

    def get_user_owned_events(self, id, **data):
        """
        GET /users/:id/owned_events/
        Returns a paginated response of :format:`events <event>`, under
        the key ``events``, of all events the user owns (i.e. events they are organising)
        """
        
        return self.get("/users/{0}/owned_events/".format(id), data=data)

    def get_user_events(self, id, **data):
        """
        GET /users/:id/events/
        Returns a paginated response of :format:`events <event>`, under
        the key ``events``, of all events the user has access to
        """

        return self.get("/users/{0}/events/".format(id), data=data)

    def get_user_venues(self, id, **data):
        """
        GET /users/:id/venues/
        Returns a paginated response of :format:`venues <venue>` objects
        that are owned by the user.
        """

        return self.get("/users/{0}/venues/".format(id), data=data)

    def get_user_organizers(self, id, **data):
        """
        GET /users/:id/organizers/
        Returns a paginated response of :format:`organizers <organizer>` objects
        that are owned by the user.
        """

        return self.get("/users/{0}/organizers/".format(id), data=data)

    def get_user_owned_event_attendees(self, id, **data):
        """
        GET /users/:id/owned_event_attendees/
        Returns a paginated response of :format:`attendees <attendee>`, under
        the key ``attendees``, of attendees visiting any of the events the user owns
        (events that would be returned from ``/users/:id/owned_events/``)
        """
        
        return self.get("/users/{0}/owned_event_attendees/".format(id), data=data)

    def get_user_owned_event_orders(self, id, **data):
        """
        GET /users/:id/owned_event_orders/
        Returns a paginated response of :format:`orders <order>`, under
        the key ``orders``, of orders placed against any of the events the user owns
        (events that would be returned from ``/users/:id/owned_events/``)
        """
        
        return self.get("/users/{0}/owned_event_orders/".format(id), data=data)

    def get_user_contact_lists(self, id, **data):
        """
        GET /users/:id/contact_lists/
        Returns a list of :format:`contact_list` that the user owns as the key
        ``contact_lists``.
        """
        
        return self.get("/users/{0}/contact_lists/".format(id), data=data)

    def post_user_contact_lists(self, id, **data):
        """
        POST /users/:id/contact_lists/
        Makes a new :format:`contact_list` for the user and returns it as
        ``contact_list``.
        """
        
        return self.post("/users/{0}/contact_lists/".format(id), data=data)

    def get_user_contact_list(self, id, contact_list_id, **data):
        """
        GET /users/:id/contact_lists/:contact_list_id/
        Gets a user's :format:`contact_list` by ID as ``contact_list``.
        """
        
        return self.get("/users/{0}/contact_lists/{1}/".format(id,contact_list_id), data=data)

    def post_user_contact_list(self, id, contact_list_id, **data):
        """
        POST /users/:id/contact_lists/:contact_list_id/
        Updates the :format:`contact_list` and returns it as ``contact_list``.
        """
        
        return self.post("/users/{0}/contact_lists/{1}/".format(id,contact_list_id), data=data)

    def delete_user_contact_list(self, id, contact_list_id, **data):
        """
        DELETE /users/:id/contact_lists/:contact_list_id/
        Deletes the contact list. Returns ``{"deleted": true}``.
        """
        
        return self.delete("/users/{0}/contact_lists/{1}/".format(id,contact_list_id), data=data)

    def get_user_contact_lists_contacts(self, id, contact_list_id, **data):
        """
        GET /users/:id/contact_lists/:contact_list_id/contacts/
        Returns the :format:`contacts <contact>` on the contact list
        as ``contacts``.
        """
        
        return self.get("/users/{0}/contact_lists/{1}/contacts/".format(id,contact_list_id), data=data)

    def post_user_contact_lists_contacts(self, id, contact_list_id, **data):
        """
        POST /users/:id/contact_lists/:contact_list_id/contacts/
        Adds a new contact to the contact list. Returns ``{"created": true}``.
        There is no way to update entries in the list; just delete the old one
        and add the updated version.
        """
        
        return self.post("/users/{0}/contact_lists/{1}/contacts/".format(id,contact_list_id), data=data)

    def delete_user_contact_lists_contacts(self, id, contact_list_id, **data):
        """
        DELETE /users/:id/contact_lists/:contact_list_id/contacts/
        Deletes the specified contact from the contact list.
        Returns ``{"deleted": true}``.
        """
        
        return self.delete("/users/{0}/contact_lists/{1}/contacts/".format(id,contact_list_id), data=data)

    def get_webhook(self, id, **data):
        """
        GET /webhooks/:id/
        Returns a :format:`webhook` for the specified webhook as ``webhook``.
        """
        
        return self.get("/webhooks/{0}/".format(id), data=data)

    def delete_webhook(self, id, **data):
        """
        DELETE /webhooks/:id/
        Deletes the specified :format:`webhook` object.
        """
        
        return self.delete("/webhooks/{0}/".format(id), data=data)

    def get_webhooks(self, **data):
        """
        GET /webhooks/
        Returns the list of :format:`webhook` objects that belong to the authenticated user.
        """
        return self.get("/webhooks/", data=data)

    def post_webhooks(self, **data):
        """
        POST /webhooks/
        .. note:: The ability to add Webhooks will be activated on or around Tuesday, January 27th, 2015.
        Parameters
        ''''''''''
        .. csv-table:: Parameters
        :header: "Name", "Type", "Required", "Description"
"endpoint_url", "string", "Yes", "The target URL of the Webhook subscription."
"event_id", "string", "No", "Represents the ID for a particular event."
"actions", "string", "No", "Determines what actions the hook is triggered for. Placing no actions in a subscription means all possible events are covered. See below for a more complete description."
        Creates a :format:`webhook` object. The ``actions`` parameter accepts a comma-seperated value that can include any or all of the following:
        * ``event.published`` - Triggered when an event is published.
        * ``event.unpublished`` - Triggered when an event is unpublished.
        * ``order.placed`` - Triggers when an order is placed for an event. Generated Webhook's API endpoint is to the Order endpoint.
        """
        return self.post("/webhooks/", data=data)
