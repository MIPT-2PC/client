from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class


# create an instance of the API class
configuration = swagger_client.Configuration()
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Nums(2.0, 5.0, operation="*")  # Nums | Nums request body (optional)

print(body)
print("\n")

try:
    # operate 2 numbers
    api_response = api_instance.operate(body=body)
    pprint(api_response)
    print("\n")
except ApiException as e:
    print("Exception when calling ApiApi->operate: %s\n" % e)


configuration = swagger_client.Configuration()
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))

try:
    # Get previous results
    api_response = api_instance.get_results()
    #pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_results: %s\n" % e)