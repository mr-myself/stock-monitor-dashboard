r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Intelligence
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CustomOperatorInstance(InstanceResource):

    class Availability(object):
        INTERNAL = "internal"
        BETA = "beta"
        PUBLIC = "public"
        RETIRED = "retired"

    """
    :ivar account_sid: The unique SID identifier of the Account the Custom Operator belongs to.
    :ivar sid: A 34 character string that uniquely identifies this Custom Operator.
    :ivar friendly_name: A human-readable name of this resource, up to 64 characters.
    :ivar description: A human-readable description of this resource, longer than the friendly name.
    :ivar author: The creator of the Custom Operator. Custom Operators can only be created by a Twilio Account.
    :ivar operator_type: Operator Type for this Operator. References an existing Operator Type resource.
    :ivar version: Numeric Custom Operator version. Incremented with each update on the resource, used to ensure integrity when updating the Custom Operator.
    :ivar availability: 
    :ivar config: Operator configuration, following the schema defined by the Operator Type. Only available on Operators created by the Account.
    :ivar date_created: The date that this Custom Operator was created, given in ISO 8601 format.
    :ivar date_updated: The date that this Custom Operator was updated, given in ISO 8601 format.
    :ivar url: The URL of this resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.description: Optional[str] = payload.get("description")
        self.author: Optional[str] = payload.get("author")
        self.operator_type: Optional[str] = payload.get("operator_type")
        self.version: Optional[int] = deserialize.integer(payload.get("version"))
        self.availability: Optional["CustomOperatorInstance.Availability"] = (
            payload.get("availability")
        )
        self.config: Optional[Dict[str, object]] = payload.get("config")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[CustomOperatorContext] = None

    @property
    def _proxy(self) -> "CustomOperatorContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CustomOperatorContext for this CustomOperatorInstance
        """
        if self._context is None:
            self._context = CustomOperatorContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the CustomOperatorInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CustomOperatorInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "CustomOperatorInstance":
        """
        Fetch the CustomOperatorInstance


        :returns: The fetched CustomOperatorInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CustomOperatorInstance":
        """
        Asynchronous coroutine to fetch the CustomOperatorInstance


        :returns: The fetched CustomOperatorInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: str,
        config: object,
        if_match: Union[str, object] = values.unset,
    ) -> "CustomOperatorInstance":
        """
        Update the CustomOperatorInstance

        :param friendly_name: A human-readable name of this resource, up to 64 characters.
        :param config: Operator configuration, following the schema defined by the Operator Type.
        :param if_match: The If-Match HTTP request header

        :returns: The updated CustomOperatorInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            config=config,
            if_match=if_match,
        )

    async def update_async(
        self,
        friendly_name: str,
        config: object,
        if_match: Union[str, object] = values.unset,
    ) -> "CustomOperatorInstance":
        """
        Asynchronous coroutine to update the CustomOperatorInstance

        :param friendly_name: A human-readable name of this resource, up to 64 characters.
        :param config: Operator configuration, following the schema defined by the Operator Type.
        :param if_match: The If-Match HTTP request header

        :returns: The updated CustomOperatorInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            config=config,
            if_match=if_match,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Intelligence.V2.CustomOperatorInstance {}>".format(context)


class CustomOperatorContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the CustomOperatorContext

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this Custom Operator.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Operators/Custom/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the CustomOperatorInstance


        :returns: True if delete succeeds, False otherwise
        """

        headers = values.of({})

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CustomOperatorInstance


        :returns: True if delete succeeds, False otherwise
        """

        headers = values.of({})

        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers
        )

    def fetch(self) -> CustomOperatorInstance:
        """
        Fetch the CustomOperatorInstance


        :returns: The fetched CustomOperatorInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = self._version.fetch(method="GET", uri=self._uri, headers=headers)

        return CustomOperatorInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> CustomOperatorInstance:
        """
        Asynchronous coroutine to fetch the CustomOperatorInstance


        :returns: The fetched CustomOperatorInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, headers=headers
        )

        return CustomOperatorInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: str,
        config: object,
        if_match: Union[str, object] = values.unset,
    ) -> CustomOperatorInstance:
        """
        Update the CustomOperatorInstance

        :param friendly_name: A human-readable name of this resource, up to 64 characters.
        :param config: Operator configuration, following the schema defined by the Operator Type.
        :param if_match: The If-Match HTTP request header

        :returns: The updated CustomOperatorInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Config": serialize.object(config),
            }
        )
        headers = values.of({})

        if not (
            if_match is values.unset or (isinstance(if_match, str) and not if_match)
        ):
            headers["If-Match"] = if_match

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return CustomOperatorInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        friendly_name: str,
        config: object,
        if_match: Union[str, object] = values.unset,
    ) -> CustomOperatorInstance:
        """
        Asynchronous coroutine to update the CustomOperatorInstance

        :param friendly_name: A human-readable name of this resource, up to 64 characters.
        :param config: Operator configuration, following the schema defined by the Operator Type.
        :param if_match: The If-Match HTTP request header

        :returns: The updated CustomOperatorInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Config": serialize.object(config),
            }
        )
        headers = values.of({})

        if not (
            if_match is values.unset or (isinstance(if_match, str) and not if_match)
        ):
            headers["If-Match"] = if_match

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return CustomOperatorInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Intelligence.V2.CustomOperatorContext {}>".format(context)


class CustomOperatorPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> CustomOperatorInstance:
        """
        Build an instance of CustomOperatorInstance

        :param payload: Payload response from the API
        """
        return CustomOperatorInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Intelligence.V2.CustomOperatorPage>"


class CustomOperatorList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CustomOperatorList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Operators/Custom"

    def create(
        self, friendly_name: str, operator_type: str, config: object
    ) -> CustomOperatorInstance:
        """
        Create the CustomOperatorInstance

        :param friendly_name: A human readable description of the new Operator, up to 64 characters.
        :param operator_type: Operator Type for this Operator. References an existing Operator Type resource.
        :param config: Operator configuration, following the schema defined by the Operator Type.

        :returns: The created CustomOperatorInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "OperatorType": operator_type,
                "Config": serialize.object(config),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return CustomOperatorInstance(self._version, payload)

    async def create_async(
        self, friendly_name: str, operator_type: str, config: object
    ) -> CustomOperatorInstance:
        """
        Asynchronously create the CustomOperatorInstance

        :param friendly_name: A human readable description of the new Operator, up to 64 characters.
        :param operator_type: Operator Type for this Operator. References an existing Operator Type resource.
        :param config: Operator configuration, following the schema defined by the Operator Type.

        :returns: The created CustomOperatorInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "OperatorType": operator_type,
                "Config": serialize.object(config),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return CustomOperatorInstance(self._version, payload)

    def stream(
        self,
        availability: Union[
            "CustomOperatorInstance.Availability", object
        ] = values.unset,
        language_code: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[CustomOperatorInstance]:
        """
        Streams CustomOperatorInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;CustomOperatorInstance.Availability&quot; availability: Returns Custom Operators with the provided availability type. Possible values: internal, beta, public, retired.
        :param str language_code: Returns Custom Operators that support the provided language code.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            availability=availability,
            language_code=language_code,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        availability: Union[
            "CustomOperatorInstance.Availability", object
        ] = values.unset,
        language_code: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[CustomOperatorInstance]:
        """
        Asynchronously streams CustomOperatorInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;CustomOperatorInstance.Availability&quot; availability: Returns Custom Operators with the provided availability type. Possible values: internal, beta, public, retired.
        :param str language_code: Returns Custom Operators that support the provided language code.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            availability=availability,
            language_code=language_code,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        availability: Union[
            "CustomOperatorInstance.Availability", object
        ] = values.unset,
        language_code: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CustomOperatorInstance]:
        """
        Lists CustomOperatorInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;CustomOperatorInstance.Availability&quot; availability: Returns Custom Operators with the provided availability type. Possible values: internal, beta, public, retired.
        :param str language_code: Returns Custom Operators that support the provided language code.
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
                availability=availability,
                language_code=language_code,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        availability: Union[
            "CustomOperatorInstance.Availability", object
        ] = values.unset,
        language_code: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CustomOperatorInstance]:
        """
        Asynchronously lists CustomOperatorInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;CustomOperatorInstance.Availability&quot; availability: Returns Custom Operators with the provided availability type. Possible values: internal, beta, public, retired.
        :param str language_code: Returns Custom Operators that support the provided language code.
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
                availability=availability,
                language_code=language_code,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        availability: Union[
            "CustomOperatorInstance.Availability", object
        ] = values.unset,
        language_code: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CustomOperatorPage:
        """
        Retrieve a single page of CustomOperatorInstance records from the API.
        Request is executed immediately

        :param availability: Returns Custom Operators with the provided availability type. Possible values: internal, beta, public, retired.
        :param language_code: Returns Custom Operators that support the provided language code.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CustomOperatorInstance
        """
        data = values.of(
            {
                "Availability": availability,
                "LanguageCode": language_code,
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
        return CustomOperatorPage(self._version, response)

    async def page_async(
        self,
        availability: Union[
            "CustomOperatorInstance.Availability", object
        ] = values.unset,
        language_code: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CustomOperatorPage:
        """
        Asynchronously retrieve a single page of CustomOperatorInstance records from the API.
        Request is executed immediately

        :param availability: Returns Custom Operators with the provided availability type. Possible values: internal, beta, public, retired.
        :param language_code: Returns Custom Operators that support the provided language code.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CustomOperatorInstance
        """
        data = values.of(
            {
                "Availability": availability,
                "LanguageCode": language_code,
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
        return CustomOperatorPage(self._version, response)

    def get_page(self, target_url: str) -> CustomOperatorPage:
        """
        Retrieve a specific page of CustomOperatorInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CustomOperatorInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CustomOperatorPage(self._version, response)

    async def get_page_async(self, target_url: str) -> CustomOperatorPage:
        """
        Asynchronously retrieve a specific page of CustomOperatorInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CustomOperatorInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CustomOperatorPage(self._version, response)

    def get(self, sid: str) -> CustomOperatorContext:
        """
        Constructs a CustomOperatorContext

        :param sid: A 34 character string that uniquely identifies this Custom Operator.
        """
        return CustomOperatorContext(self._version, sid=sid)

    def __call__(self, sid: str) -> CustomOperatorContext:
        """
        Constructs a CustomOperatorContext

        :param sid: A 34 character string that uniquely identifies this Custom Operator.
        """
        return CustomOperatorContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Intelligence.V2.CustomOperatorList>"
