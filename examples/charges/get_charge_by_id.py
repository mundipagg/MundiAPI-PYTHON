from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "sk_test_EegqODfvktNJn4YA:"
charges_controller = charges_controller.ChargesController()

chargeId = "ch_8YQ1JeTLzF8zlqWy"

try:
    result = charges_controller.get_charge(chargeId)
    assert result is not None
    assert result.id == chargeId
    print("Charge found!")
    print("Charge_Id: ", result.id)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex


