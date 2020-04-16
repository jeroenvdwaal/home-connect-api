# home_connect_api.SettingsApi

All URIs are relative to *https://api.home-connect.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting**](SettingsApi.md#get_setting) | **GET** /homeappliances/{haid}/settings/{settingkey} | Get a specific setting
[**get_settings**](SettingsApi.md#get_settings) | **GET** /homeappliances/{haid}/settings | Get a list of available settings
[**set_setting**](SettingsApi.md#set_setting) | **PUT** /homeappliances/{haid}/settings/{settingkey} | Set a specific setting

# **get_setting**
> GetSetting get_setting(haid, settingkey, accept_language=accept_language)

Get a specific setting

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
api_instance = home_connect_api.SettingsApi(home_connect_api.ApiClient(configuration))
haid = 'haid_example' # str | ID of home appliance
settingkey = 'settingkey_example' # str | ID of the setting
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

try:
    # Get a specific setting
    api_response = api_instance.get_setting(haid, settingkey, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **settingkey** | **str**| ID of the setting | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**GetSetting**](GetSetting.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> ArrayOfSettings get_settings(haid, accept_language=accept_language)

Get a list of available settings

Get a list of available setting of the home appliance.  Further documentation can be found here: * [Power state](https://developer.home-connect.com/docs/settings/power_state) * [Fridge temperature](https://developer.home-connect.com/docs/api/settings/fridgetemperature) * [Fridge super mode](https://developer.home-connect.com/docs/api/settings/fridgesupermode) * [Freezer temperature](https://developer.home-connect.com/docs/api/settings/freezertemperature) * [Freezer super mode](https://developer.home-connect.com/docs/api/settings/freezersupermode) 

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
api_instance = home_connect_api.SettingsApi(home_connect_api.ApiClient(configuration))
haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

try:
    # Get a list of available settings
    api_response = api_instance.get_settings(haid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**ArrayOfSettings**](ArrayOfSettings.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_setting**
> set_setting(body, haid, settingkey, accept_language=accept_language)

Set a specific setting

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
api_instance = home_connect_api.SettingsApi(home_connect_api.ApiClient(configuration))
body = home_connect_api.PutSetting() # PutSetting | description of the setting
haid = 'haid_example' # str | ID of home appliance
settingkey = 'settingkey_example' # str | ID of the setting
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

try:
    # Set a specific setting
    api_instance.set_setting(body, haid, settingkey, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling SettingsApi->set_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSetting**](PutSetting.md)| description of the setting | 
 **haid** | **str**| ID of home appliance | 
 **settingkey** | **str**| ID of the setting | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

void (empty response body)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: application/vnd.bsh.sdk.v1+json
 - **Accept**: application/vnd.bsh.sdk.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

