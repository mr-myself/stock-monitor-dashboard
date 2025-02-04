r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ChannelSenderInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ChannelSender resource.
    :ivar messaging_service_sid: The SID of the [Service](https://www.twilio.com/docs/messaging/services) the resource is associated with.
    :ivar sid: The unique string that we created to identify the ChannelSender resource.
    :ivar sender: The unique string that identifies the sender e.g whatsapp:+123456XXXX.
    :ivar sender_type: A string value that identifies the sender type e.g WhatsApp, Messenger.
    :ivar country_code: The 2-character [ISO Country Code](https://www.iso.org/iso-3166-country-codes.html) of the number.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the ChannelSender resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        messaging_service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.messaging_service_sid: Optional[str] = payload.get("messaging_service_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.sender: Optional[str] = payload.get("sender")
        self.sender_type: Optional[str] = payload.get("sender_type")
        self.country_code: Optional[str] = payload.get("country_code")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "messaging_service_sid": messaging_service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[ChannelSenderContext] = None

    @property
    def _proxy(self) -> "ChannelSenderContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ChannelSenderContext for this ChannelSenderInstance
        """
        if self._context is None:
            self._context = ChannelSenderContext(
                self._version,
                messaging_service_sid=self._solution["messaging_service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ChannelSenderInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ChannelSenderInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ChannelSenderInstance":
        """
        Fetch the ChannelSenderInstance


        :returns: The fetched ChannelSenderInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ChannelSenderInstance":
        """
        Asynchronous coroutine to fetch the ChannelSenderInstance


        :returns: The fetched ChannelSenderInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.ChannelSenderInstance {}>".format(context)


class ChannelSenderContext(InstanceContext):

    def __init__(self, version: Version, messaging_service_sid: str, sid: str):
        """
        Initialize the ChannelSenderContext

        :param version: Version that contains the resource
        :param messaging_service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.
        :param sid: The SID of the ChannelSender resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "messaging_service_sid": messaging_service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{messaging_service_sid}/ChannelSenders/{sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the ChannelSenderInstance


        :returns: True if delete succeeds, False otherwise
        """

        headers = values.of({})

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ChannelSenderInstance


        :returns: True if delete succeeds, False otherwise
        """

        headers = values.of({})

        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers
        )

    def fetch(self) -> ChannelSenderInstance:
        """
        Fetch the ChannelSenderInstance


        :returns: The fetched ChannelSenderInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = self._version.fetch(method="GET", uri=self._uri, headers=headers)

        return ChannelSenderInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ChannelSenderInstance:
        """
        Asynchronous coroutine to fetch the ChannelSenderInstance


        :returns: The fetched ChannelSenderInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, headers=headers
        )

        return ChannelSenderInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.ChannelSenderContext {}>".format(context)


class ChannelSenderPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> ChannelSenderInstance:
        """
        Build an instance of ChannelSenderInstance

        :param payload: Payload response from the API
        """
        return ChannelSenderInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.ChannelSenderPage>"


class ChannelSenderList(ListResource):

    def __init__(self, version: Version, messaging_service_sid: str):
        """
        Initialize the ChannelSenderList

        :param version: Version that contains the resource
        :param messaging_service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "messaging_service_sid": messaging_service_sid,
        }
        self._uri = "/Services/{messaging_service_sid}/ChannelSenders".format(
            **self._solution
        )

    def create(self, sid: str) -> ChannelSenderInstance:
        """
        Create the ChannelSenderInstance

        :param sid: The SID of the Channel Sender being added to the Service.

        :returns: The created ChannelSenderInstance
        """

        data = values.of(
            {
                "Sid": sid,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ChannelSenderInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
        )

    async def create_async(self, sid: str) -> ChannelSenderInstance:
        """
        Asynchronously create the ChannelSenderInstance

        :param sid: The SID of the Channel Sender being added to the Service.

        :returns: The created ChannelSenderInstance
        """

        data = values.of(
            {
                "Sid": sid,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ChannelSenderInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ChannelSenderInstance]:
        """
        Streams ChannelSenderInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[ChannelSenderInstance]:
        """
        Asynchronously streams ChannelSenderInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ChannelSenderInstance]:
        """
        Lists ChannelSenderInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ChannelSenderInstance]:
        """
        Asynchronously lists ChannelSenderInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ChannelSenderPage:
        """
        Retrieve a single page of ChannelSenderInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelSenderInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = self._version.page(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return ChannelSenderPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ChannelSenderPage:
        """
        Asynchronously retrieve a single page of ChannelSenderInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelSenderInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return ChannelSenderPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> ChannelSenderPage:
        """
        Retrieve a specific page of ChannelSenderInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ChannelSenderInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ChannelSenderPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> ChannelSenderPage:
        """
        Asynchronously retrieve a specific page of ChannelSenderInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ChannelSenderInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ChannelSenderPage(self._version, response, self._solution)

    def get(self, sid: str) -> ChannelSenderContext:
        """
        Constructs a ChannelSenderContext

        :param sid: The SID of the ChannelSender resource to fetch.
        """
        return ChannelSenderContext(
            self._version,
            messaging_service_sid=self._solution["messaging_service_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> ChannelSenderContext:
        """
        Constructs a ChannelSenderContext

        :param sid: The SID of the ChannelSender resource to fetch.
        """
        return ChannelSenderContext(
            self._version,
            messaging_service_sid=self._solution["messaging_service_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.ChannelSenderList>"
