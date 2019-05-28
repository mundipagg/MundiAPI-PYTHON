from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
customers_controller = customers_controller.CustomersController()

request = create_customer_request.CreateCustomerRequest()
request.name = "sdk customer test"
request.email = "tonystark@avengers.com"

try:
    result = customers_controller.create_customer(request)
    assert result is not None
    print("Customer id: ", result.id)

except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex




