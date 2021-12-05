# swagger_client.InteractionApi

All URIs are relative to *http://localhost:8080/MIPT-2PC/preprocessor/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_table**](InteractionApi.md#get_table) | **GET** /getTable | hello message to get preprocessed data
[**start2_pc**](InteractionApi.md#start2_pc) | **POST** /start2PC | start preprocessing procedure

# **get_table**
> list[Table] get_table()

hello message to get preprocessed data

Returns preprocessed table for this user, masked input and outputs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InteractionApi()

try:
    # hello message to get preprocessed data
    api_response = api_instance.get_table()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->get_table: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Table]**](Table.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start2_pc**
> list[Table] start2_pc(body=body)

start preprocessing procedure

send config file to start preprocessing

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InteractionApi()
body = swagger_client.Table() # Table | Nums request body (optional)

try:
    # start preprocessing procedure
    api_response = api_instance.start2_pc(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->start2_pc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Table**](Table.md)| Nums request body | [optional] 

### Return type

[**list[Table]**](Table.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

