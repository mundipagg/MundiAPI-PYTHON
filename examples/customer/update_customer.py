from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "YOUR_SECRET_KEY:"
customers_controller = customers_controller.CustomersController()

createRequest = create_customer_request.CreateCustomerRequest()
createRequest.name = "sdk customer test"
createRequest.email = "tonystark@avengers.com"

updateRequest = update_customer_request.UpdateCustomerRequest()
updateRequest.name = "New Customer Name"

try:
    result = customers_controller.create_customer(createRequest)
    customers_controller.update_customer(result.id, updateRequest)
    updatedCustomer = customers_controller.get_customer(result.id)
    assert result is not None
    assert updatedCustomer is not None
    assert result.id == updatedCustomer.id
    assert createRequest.name != updatedCustomer.name
    assert updatedCustomer.name == updateRequest.name
    print("Customer id: ", updatedCustomer.id)
    print("Old name: ", createRequest.name)
    print("New name: ", updatedCustomer.name)

except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex




