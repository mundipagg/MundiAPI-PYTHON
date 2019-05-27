from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.controllers import *
from mundiapi.exceptions.error_exception import *

MundiapiClient.config.basic_auth_user_name = "SUA_SECRET_KEY:"
orders_controller = orders_controller.OrdersController()

try:
    result = orders_controller.get_order("or_5dak14yI3fy4RL72")
    assert result is not None
    assert result.id is not None
    print("Order id: ", result.id)
    print("Order result status: ", result.status)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex
