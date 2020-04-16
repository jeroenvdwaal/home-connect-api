# home_connect_api.CommandsApi

All URIs are relative to *https://api.home-connect.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_commands**](CommandsApi.md#get_available_commands) | **GET** /homeappliances/{haid}/commands | Get a list of supported commands of the home appliance
[**put_command**](CommandsApi.md#put_command) | **PUT** /homeappliances/{haid}/commands/{commandkey} | Execute a specific command of the home appliance

# **get_available_commands**
> get_available_commands(haid, accept_language=accept_language)

Get a list of supported commands of the home appliance

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
api_instance = home_connect_api.CommandsApi(home_connect_api.ApiClient(configuration))
haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

try:
    # Get a list of supported commands of the home appliance
    api_instance.get_available_commands(haid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling CommandsApi->get_available_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

void (empty response body)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_command**
> put_command(body, haid, commandkey, accept_language=accept_language)

Execute a specific command of the home appliance

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
api_instance = home_connect_api.CommandsApi(home_connect_api.ApiClient(configuration))
body = home_connect_api.Command() # Command | description of the command to send
haid = 'haid_example' # str | ID of home appliance
commandkey = 'commandkey_example' # str | feature key of the command
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

try:
    # Execute a specific command of the home appliance
    api_instance.put_command(body, haid, commandkey, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling CommandsApi->put_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Command**](Command.md)| description of the command to send | 
 **haid** | **str**| ID of home appliance | 
 **commandkey** | **str**| feature key of the command | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

void (empty response body)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: application/vnd.bsh.sdk.v1+json
 - **Accept**: application/vnd.bsh.sdk.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

