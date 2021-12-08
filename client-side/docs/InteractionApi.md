# swagger_client_pre.InteractionApi

All URIs are relative to *http://localhost:8080/MIPT-2PC/user/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_out**](InteractionApi.md#exchange_out) | **POST** /exchangeOut | Exchange calculated nodes with self table from Nth layer
[**hello**](InteractionApi.md#hello) | **GET** /hello | hello message to neighbour

# **exchange_out**
> list[ExchangePayload] exchange_out(body=body)

Exchange calculated nodes with self table from Nth layer

Exchange calculated nodes with self table from Nth layer

### Example
```python
from __future__ import print_function
import time
import swagger_client_pre
from swagger_client_pre.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client_pre.InteractionApi()
body = swagger_client_pre.ExchangePayload() # ExchangePayload | calculated payload to send to neighbour in Decimal representation (optional)

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
> InlineResponse200 hello()

hello message to neighbour

Returns hello message

### Example
```python
from __future__ import print_function
import time
import swagger_client_pre
from swagger_client_pre.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client_pre.InteractionApi()

try:
    # hello message to neighbour
    api_response = api_instance.hello()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InteractionApi->hello: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

