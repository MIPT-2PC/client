# swagger_client.ApiApi

All URIs are relative to *https://localhost:8080/MIPT-2PC/preprocessor/0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_results**](ApiApi.md#get_results) | **GET** /results | Get previous results
[**operate**](ApiApi.md#operate) | **POST** /operate | operate 2 numbers

# **get_results**
> list[Results] get_results()

Get previous results

retrieve results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi()

try:
    # Get previous results
    api_response = api_instance.get_results()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_results: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Results]**](Results.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operate**
> list[Nums] operate(body=body)

operate 2 numbers

operate 2 numbers with defined action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi()
body = swagger_client.Nums() # Nums | Nums request body (optional)

try:
    # operate 2 numbers
    api_response = api_instance.operate(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->operate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Nums**](Nums.md)| Nums request body | [optional] 

### Return type

[**list[Nums]**](Nums.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

