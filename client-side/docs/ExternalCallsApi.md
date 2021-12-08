# swagger_client.ExternalCallsApi

All URIs are relative to *http://localhost:8080/MIPT-2PC/user/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_result**](ExternalCallsApi.md#get_result) | **GET** /getResult | returns calculated with 2PC result
[**init**](ExternalCallsApi.md#init) | **POST** /init | Init call to start 2PC process.

# **get_result**
> list[Answer] get_result()

returns calculated with 2PC result

Returns the result of computation on config with A & B inputs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExternalCallsApi()

try:
    # returns calculated with 2PC result
    api_response = api_instance.get_result()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalCallsApi->get_result: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Answer]**](Answer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init**
> init(input_number=input_number, config=config)

Init call to start 2PC process.

Consumes input data for this user and config location

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExternalCallsApi()
input_number = 56 # int |  (optional)
config = 'config_example' # str |  (optional)

try:
    # Init call to start 2PC process.
    api_instance.init(input_number=input_number, config=config)
except ApiException as e:
    print("Exception when calling ExternalCallsApi->init: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_number** | **int**|  | [optional] 
 **config** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

