# swagger_client.InteractionApi

All URIs are relative to *http://localhost:8080/MIPT-2PC/user/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_out**](InteractionApi.md#exchange_out) | **POST** /exchangeOut | Exchange calculated nodes with self table from Nth layer
[**hello**](InteractionApi.md#hello) | **GET** /hello | hello message to get preprocessed data

# **exchange_out**
> list[ExchangePayload] exchange_out(body=body)

Exchange calculated nodes with self table from Nth layer

Exchange calculated nodes with self table from Nth layer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InteractionApi()
body = swagger_client.ExchangePayload() # ExchangePayload | calculated payload to send to neighbour in Decimal representation (optional)

try:
    # Exchange calculated nodes with self table from Nth layer
    api_response = api_instance.exchange_out(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->exchange_out: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExchangePayload**](ExchangePayload.md)| calculated payload to send to neighbour in Decimal representation | [optional] 

### Return type

[**list[ExchangePayload]**](ExchangePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hello**
> list[Table] hello()

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
    api_response = api_instance.hello()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->hello: %s\n" % e)
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

