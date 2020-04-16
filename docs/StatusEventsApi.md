# home_connect_api.StatusEventsApi

All URIs are relative to *https://api.home-connect.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_events**](StatusEventsApi.md#get_all_events) | **GET** /homeappliances/events | Get stream of events for all appliances - NOT WORKING WITH SWAGGER
[**get_events**](StatusEventsApi.md#get_events) | **GET** /homeappliances/{haid}/events | Get stream of events for one appliance - NOT WORKING WITH SWAGGER
[**get_status**](StatusEventsApi.md#get_status) | **GET** /homeappliances/{haid}/status | Get current status of home appliance
[**get_status_value**](StatusEventsApi.md#get_status_value) | **GET** /homeappliances/{haid}/status/{statuskey} | Get current status of home appliance

# **get_all_events**
> ArrayOfEvents get_all_events(accept_language=accept_language)

Get stream of events for all appliances - NOT WORKING WITH SWAGGER

Server Sent Events are available as Eventsource API in JavaScript and are implemented by various HTTP client libraries and tools including curl.  Unfortunately, SSE is not compatible to OpenAPI specs and can therefore not be properly specified within this API description.  An SSE event contains three parts separated by linebreaks: event, data and id. Different events are separated by empty lines.  The event field can be one of these types: KEEP-ALIVE, STATUS, EVENT, NOTIFY, DISCONNECTED, CONNECTED.  In case of the event type being STATUS, EVENT or NOTIFY, the \"data\" field is populated with the JSON object defined below.  The id contains the home appliance ID.  Further documentation can be found here: * [Events availability matrix](https://developer.home-connect.com/docs/monitoring/availabilitymatrix) * [Program changes](https://developer.home-connect.com/docs/monitoring/program_option_changes) * [Option changes](https://developer.home-connect.com/docs/monitoring/option_changes) * [Program progress changes](https://developer.home-connect.com/docs/monitoring/program_progress_changes) * [Home appliance state changes](https://developer.home-connect.com/docs/monitoring/appliance_state_changes) 

### Example
```python
from __future__ import print_function
import time
import home_connect_api
from home_connect_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: homeconnect_auth
configuration = home_connect_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = home_connect_api.StatusEventsApi(home_connect_api.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

try:
    # Get stream of events for all appliances - NOT WORKING WITH SWAGGER
    api_response = api_instance.get_all_events(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusEventsApi->get_all_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**ArrayOfEvents**](ArrayOfEvents.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> ArrayOfEvents get_events(haid, accept_language=accept_language, accept=accept)

Get stream of events for one appliance - NOT WORKING WITH SWAGGER

If you want to do a one-time query of the current status, you can ask for the content-type `application/vnd.bsh.sdk.v1+json` and get the status as normal HTTP response.  If you want an ongoing stream of events in real time, ask for the content type `text/event-stream` and you'll get a stream as Server Sent Events.  Server Sent Events are available as Eventsource API in JavaScript and are implemented by various HTTP client libraries and tools including curl.  Unfortunately, SSE is not compatible to OpenAPI specs and can therefore not be properly specified within this API description.  An SSE event contains three parts separated by linebreaks: event, data and id. Different events are separated by empty lines.  The event field can be one of these types: KEEP-ALIVE, STATUS, EVENT, NOTIFY, DISCONNECTED, CONNECTED.  In case of the event type being STATUS, EVENT or NOTIFY, the \"data\" field is populated with the JSON object defined below.  The id contains the home appliance ID.  Further documentation can be found here: * [Events availability matrix](https://developer.home-connect.com/docs/monitoring/availabilitymatrix) * [Program changes](https://developer.home-connect.com/docs/monitoring/program_option_changes) * [Option changes](https://developer.home-connect.com/docs/monitoring/option_changes) * [Program progress changes](https://developer.home-connect.com/docs/monitoring/program_progress_changes) * [Home appliance state changes](https://developer.home-connect.com/docs/monitoring/appliance_state_changes) 

### Example
```python
from __future__ import print_function
import time
import home_connect_api
from home_connect_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: homeconnect_auth
configuration = home_connect_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = home_connect_api.StatusEventsApi(home_connect_api.ApiClient(configuration))
haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)
accept = 'accept_example' # str |  (optional)

try:
    # Get stream of events for one appliance - NOT WORKING WITH SWAGGER
    api_response = api_instance.get_events(haid, accept_language=accept_language, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusEventsApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**ArrayOfEvents**](ArrayOfEvents.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json, text/event-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> ArrayOfStatus get_status(haid, accept_language=accept_language)

Get current status of home appliance

A detailed description of the available status can be found here:  * [Remote control activation state](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate) * [Remote start allowance state](https://developer.home-connect.com/docs/api/status/remotestartallowancestate) * [Local control state](https://developer.home-connect.com/docs/api/status/localcontrolstate) * [Operation state](https://developer.home-connect.com/docs/status/operation_state) * [Door state](https://developer.home-connect.com/docs/status/door_state)  Several more device-specific states can be found [in the documentation](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate). 

### Example
```python
from __future__ import print_function
import time
import home_connect_api
from home_connect_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: homeconnect_auth
configuration = home_connect_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = home_connect_api.StatusEventsApi(home_connect_api.ApiClient(configuration))
haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

try:
    # Get current status of home appliance
    api_response = api_instance.get_status(haid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusEventsApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**ArrayOfStatus**](ArrayOfStatus.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_value**
> Status get_status_value(haid, statuskey, accept_language=accept_language)

Get current status of home appliance

A detailed description of the available status can be found here:  * [Remote control activation state](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate) * [Remote start allowance state](https://developer.home-connect.com/docs/api/status/remotestartallowancestate) * [Local control state](https://developer.home-connect.com/docs/api/status/localcontrolstate) * [Operation state](https://developer.home-connect.com/docs/status/operation_state) * [Door state](https://developer.home-connect.com/docs/status/door_state)  Several more device-specific states can be found [in the documentation](https://developer.home-connect.com/docs/api/status/remotecontrolactivationstate). 

### Example
```python
from __future__ import print_function
import time
import home_connect_api
from home_connect_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: homeconnect_auth
configuration = home_connect_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = home_connect_api.StatusEventsApi(home_connect_api.ApiClient(configuration))
haid = 'haid_example' # str | ID of home appliance
statuskey = 'statuskey_example' # str | key of the specific status to get
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

try:
    # Get current status of home appliance
    api_response = api_instance.get_status_value(haid, statuskey, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusEventsApi->get_status_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **statuskey** | **str**| key of the specific status to get | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

