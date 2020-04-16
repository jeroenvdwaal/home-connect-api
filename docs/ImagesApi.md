# home_connect_api.ImagesApi

All URIs are relative to *https://api.home-connect.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image**](ImagesApi.md#get_image) | **GET** /homeappliances/{haid}/images/{imagekey} | Get a specific image
[**get_images**](ImagesApi.md#get_images) | **GET** /homeappliances/{haid}/images | Get a list of available images

# **get_image**
> get_image(haid, imagekey)

Get a specific image

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
api_instance = home_connect_api.ImagesApi(home_connect_api.ApiClient(configuration))
haid = 'haid_example' # str | ID of home appliance
imagekey = 'imagekey_example' # str | ID of the image

try:
    # Get a specific image
    api_instance.get_image(haid, imagekey)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **imagekey** | **str**| ID of the image | 

### Return type

void (empty response body)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> ArrayOfImages get_images(haid, accept_language=accept_language)

Get a list of available images

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
api_instance = home_connect_api.ImagesApi(home_connect_api.ApiClient(configuration))
haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

try:
    # Get a list of available images
    api_response = api_instance.get_images(haid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**ArrayOfImages**](ArrayOfImages.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

