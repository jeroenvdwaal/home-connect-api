# coding: utf-8

"""
    Home Connect API

    This API provides access to home appliances enabled by Home Connect (https://home-connect.com). Through the API programs can be started and stopped, or home appliances configured and monitored. For instance, you can start a cotton program on a washer and get a notification when the cycle is complete.  To get started with this web client, visit https://developer.home-connect.com and register an account. An application with a client ID for this API client will be automatically generated for you.  In order to use this API in your own client, you need an OAuth 2 client implementing the authorization code grant flow (https://developer.home-connect.com/docs/authorization/flow).   More details can be found here: https://www.rfc-editor.org/rfc/rfc6749.txt  Authorization URL: https://api.home-connect.com/security/oauth/authorize  Token URL: https://api.home-connect.com/security/oauth/token   # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from home_connect_api.api_client import ApiClient


class StatusEventsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_events(self, **kwargs):  # noqa: E501
        """Get stream of events for all appliances - NOT WORKING WITH SWAGGER  # noqa: E501

        Server Sent Events are available as Eventsource API in JavaScript and are implemented by various HTTP client libraries and tools including curl.  Unfortunately, SSE is not compatible to OpenAPI specs and can therefore not be properly specified within this API description.  An SSE event contains three parts separated by linebreaks: event, data and id. Different events are separated by empty lines.  The event field can be one of these types: KEEP-ALIVE, STATUS, EVENT, NOTIFY, DISCONNECTED, CONNECTED.  In case of the event type being STATUS, EVENT or NOTIFY, the \"data\" field is populated with the JSON object defined below.  The id contains the home appliance ID.  Further documentation can be found here: * [Events availability matrix](https://developer.home-connect.com/docs/monitoring/availabilitymatrix) * [Program changes](https://developer.home-connect.com/docs/monitoring/program_option_changes) * [Option changes](https://developer.home-connect.com/docs/monitoring/option_changes) * [Program progress changes](https://developer.home-connect.com/docs/monitoring/program_progress_changes) * [Home appliance state changes](https://developer.home-connect.com/docs/monitoring/appliance_state_changes)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_events(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept_language: Language for localized assets
        :return: ArrayOfEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_events_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_events_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_events_with_http_info(self, **kwargs):  # noqa: E501
        """Get stream of events for all appliances - NOT WORKING WITH SWAGGER  # noqa: E501

        Server Sent Events are available as Eventsource API in JavaScript and are implemented by various HTTP client libraries and tools including curl.  Unfortunately, SSE is not compatible to OpenAPI specs and can therefore not be properly specified within this API description.  An SSE event contains three parts separated by linebreaks: event, data and id. Different events are separated by empty lines.  The event field can be one of these types: KEEP-ALIVE, STATUS, EVENT, NOTIFY, DISCONNECTED, CONNECTED.  In case of the event type being STATUS, EVENT or NOTIFY, the \"data\" field is populated with the JSON object defined below.  The id contains the home appliance ID.  Further documentation can be found here: * [Events availability matrix](https://developer.home-connect.com/docs/monitoring/availabilitymatrix) * [Program changes](https://developer.home-connect.com/docs/monitoring/program_option_changes) * [Option changes](https://developer.home-connect.com/docs/monitoring/option_changes) * [Program progress changes](https://developer.home-connect.com/docs/monitoring/program_progress_changes) * [Home appliance state changes](https://developer.home-connect.com/docs/monitoring/appliance_state_changes)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_events_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept_language: Language for localized assets
        :return: ArrayOfEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_events" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/event-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['homeconnect_auth']  # noqa: E501

        return self.api_client.call_api(
            '/homeappliances/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArrayOfEvents',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_events(self, haid, **kwargs):  # noqa: E501
        """Get stream of events for one appliance - NOT WORKING WITH SWAGGER  # noqa: E501

        If you want to do a one-time query of the current status, you can ask for the content-type `application/vnd.bsh.sdk.v1+json` and get the status as normal HTTP response.  If you want an ongoing stream of events in real time, ask for the content type `text/event-stream` and you'll get a stream as Server Sent Events.  Server Sent Events are available as Eventsource API in JavaScript and are implemented by various HTTP client libraries and tools including curl.  Unfortunately, SSE is not compatible to OpenAPI specs and can therefore not be properly specified within this API description.  An SSE event contains three parts separated by linebreaks: event, data and id. Different events are separated by empty lines.  The event field can be one of these types: KEEP-ALIVE, STATUS, EVENT, NOTIFY, DISCONNECTED, CONNECTED.  In case of the event type being STATUS, EVENT or NOTIFY, the \"data\" field is populated with the JSON object defined below.  The id contains the home appliance ID.  Further documentation can be found here: * [Events availability matrix](https://developer.home-connect.com/docs/monitoring/availabilitymatrix) * [Program changes](https://developer.home-connect.com/docs/monitoring/program_option_changes) * [Option changes](https://developer.home-connect.com/docs/monitoring/option_changes) * [Program progress changes](https://developer.home-connect.com/docs/monitoring/program_progress_changes) * [Home appliance state changes](https://developer.home-connect.com/docs/monitoring/appliance_state_changes)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events(haid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str haid: ID of home appliance (required)
        :param str accept_language: Language for localized assets
        :param str accept:
        :return: ArrayOfEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_events_with_http_info(haid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_events_with_http_info(haid, **kwargs)  # noqa: E501
            return data

    def get_events_with_http_info(self, haid, **kwargs):  # noqa: E501
        """Get stream of events for one appliance - NOT WORKING WITH SWAGGER  # noqa: E501

        If you want to do a one-time query of the current status, you can ask for the content-type `application/vnd.bsh.sdk.v1+json` and get the status as normal HTTP response.  If you want an ongoing stream of events in real time, ask for the content type `text/event-stream` and you'll get a stream as Server Sent Events.  Server Sent Events are available as Eventsource API in JavaScript and are implemented by various HTTP client libraries and tools including curl.  Unfortunately, SSE is not compatible to OpenAPI specs and can therefore not be properly specified within this API description.  An SSE event contains three parts separated by linebreaks: event, data and id. Different events are separated by empty lines.  The event field can be one of these types: KEEP-ALIVE, STATUS, EVENT, NOTIFY, DISCONNECTED, CONNECTED.  In case of the event type being STATUS, EVENT or NOTIFY, the \"data\" field is populated with the JSON object defined below.  The id contains the home appliance ID.  Further documentation can be found here: * [Events availability matrix](https://developer.home-connect.com/docs/monitoring/availabilitymatrix) * [Program changes](https://developer.home-connect.com/docs/monitoring/program_option_changes) * [Option changes](https://developer.home-connect.com/docs/monitoring/option_changes) * [Program progress changes](https://developer.home-connect.com/docs/monitoring/program_progress_changes) * [Home appliance state changes](https://developer.home-connect.com/docs/monitoring/appliance_state_changes)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_with_http_info(haid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str haid: ID of home appliance (required)
        :param str accept_language: Language for localized assets
        :param str accept:
        :return: ArrayOfEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['haid', 'accept_language', 'accept']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'haid' is set
        if ('haid' not in params or
                params['haid'] is None):
            raise ValueError("Missing the required parameter `haid` when calling `get_events`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'haid' in params:
            path_params['haid'] = params['haid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.bsh.sdk.v1+json', 'text/event-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['homeconnect_auth']  # noqa: E501

        return self.api_client.call_api(
            '/homeappliances/{haid}/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArrayOfEvents',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_status(self, haid, **kwargs):  # noqa: E501
        """Get current status of home appliance  # noqa: E501

        A detailed description of the available status can be found here:  * [Remote control activation state](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate) * [Remote start allowance state](https://developer.home-connect.com/docs/api/status/remotestartallowancestate) * [Local control state](https://developer.home-connect.com/docs/api/status/localcontrolstate) * [Operation state](https://developer.home-connect.com/docs/status/operation_state) * [Door state](https://developer.home-connect.com/docs/status/door_state)  Several more device-specific states can be found [in the documentation](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status(haid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str haid: ID of home appliance (required)
        :param str accept_language: Language for localized assets
        :return: ArrayOfStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_status_with_http_info(haid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_status_with_http_info(haid, **kwargs)  # noqa: E501
            return data

    def get_status_with_http_info(self, haid, **kwargs):  # noqa: E501
        """Get current status of home appliance  # noqa: E501

        A detailed description of the available status can be found here:  * [Remote control activation state](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate) * [Remote start allowance state](https://developer.home-connect.com/docs/api/status/remotestartallowancestate) * [Local control state](https://developer.home-connect.com/docs/api/status/localcontrolstate) * [Operation state](https://developer.home-connect.com/docs/status/operation_state) * [Door state](https://developer.home-connect.com/docs/status/door_state)  Several more device-specific states can be found [in the documentation](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_with_http_info(haid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str haid: ID of home appliance (required)
        :param str accept_language: Language for localized assets
        :return: ArrayOfStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['haid', 'accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'haid' is set
        if ('haid' not in params or
                params['haid'] is None):
            raise ValueError("Missing the required parameter `haid` when calling `get_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'haid' in params:
            path_params['haid'] = params['haid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.bsh.sdk.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['homeconnect_auth']  # noqa: E501

        return self.api_client.call_api(
            '/homeappliances/{haid}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArrayOfStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_status_value(self, haid, statuskey, **kwargs):  # noqa: E501
        """Get current status of home appliance  # noqa: E501

        A detailed description of the available status can be found here:  * [Remote control activation state](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate) * [Remote start allowance state](https://developer.home-connect.com/docs/api/status/remotestartallowancestate) * [Local control state](https://developer.home-connect.com/docs/api/status/localcontrolstate) * [Operation state](https://developer.home-connect.com/docs/status/operation_state) * [Door state](https://developer.home-connect.com/docs/status/door_state)  Several more device-specific states can be found [in the documentation](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_value(haid, statuskey, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str haid: ID of home appliance (required)
        :param str statuskey: key of the specific status to get (required)
        :param str accept_language: Language for localized assets
        :return: Status
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_status_value_with_http_info(haid, statuskey, **kwargs)  # noqa: E501
        else:
            (data) = self.get_status_value_with_http_info(haid, statuskey, **kwargs)  # noqa: E501
            return data

    def get_status_value_with_http_info(self, haid, statuskey, **kwargs):  # noqa: E501
        """Get current status of home appliance  # noqa: E501

        A detailed description of the available status can be found here:  * [Remote control activation state](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate) * [Remote start allowance state](https://developer.home-connect.com/docs/api/status/remotestartallowancestate) * [Local control state](https://developer.home-connect.com/docs/api/status/localcontrolstate) * [Operation state](https://developer.home-connect.com/docs/status/operation_state) * [Door state](https://developer.home-connect.com/docs/status/door_state)  Several more device-specific states can be found [in the documentation](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_value_with_http_info(haid, statuskey, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str haid: ID of home appliance (required)
        :param str statuskey: key of the specific status to get (required)
        :param str accept_language: Language for localized assets
        :return: Status
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['haid', 'statuskey', 'accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_status_value" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'haid' is set
        if ('haid' not in params or
                params['haid'] is None):
            raise ValueError("Missing the required parameter `haid` when calling `get_status_value`")  # noqa: E501
        # verify the required parameter 'statuskey' is set
        if ('statuskey' not in params or
                params['statuskey'] is None):
            raise ValueError("Missing the required parameter `statuskey` when calling `get_status_value`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'haid' in params:
            path_params['haid'] = params['haid']  # noqa: E501
        if 'statuskey' in params:
            path_params['statuskey'] = params['statuskey']  # noqa: E501

        query_params = []

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.bsh.sdk.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['homeconnect_auth']  # noqa: E501

        return self.api_client.call_api(
            '/homeappliances/{haid}/status/{statuskey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Status',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)