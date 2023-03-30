
# Get Usage Response

Response object for getting a usage

## Structure

`GetUsageResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | Id |
| `quantity` | `int` | Required | Quantity |
| `description` | `string` | Required | Description |
| `used_at` | `datetime` | Required | Used at |
| `created_at` | `datetime` | Required | Creation date |
| `status` | `string` | Required | Status |
| `deleted_at` | `datetime` | Optional | - |
| `subscription_item` | [`GetSubscriptionItemResponse`](../../doc/models/get-subscription-item-response.md) | Required | Subscription item |
| `code` | `string` | Optional | Identification code in the client system |
| `group` | `string` | Optional | Identification group in the client system |
| `amount` | `int` | Optional | Field used in item scheme type 'Percent' |

## Example (as JSON)

```json
{
  "id": "id0",
  "quantity": 68,
  "description": "description0",
  "used_at": "2016-03-13T12:52:32.123Z",
  "created_at": "2016-03-13T12:52:32.123Z",
  "status": "status8",
  "deleted_at": null,
  "subscription_item": {
    "id": "id6",
    "description": "description4",
    "status": "status2",
    "created_at": "2016-03-13T12:52:32.123Z",
    "updated_at": "2016-03-13T12:52:32.123Z",
    "pricing_scheme": {
      "price": 178,
      "scheme_type": "scheme_type2",
      "price_brackets": [
        {
          "start_quantity": 131,
          "price": 69,
          "end_quantity": null,
          "overage_price": null
        }
      ],
      "minimum_price": null,
      "percentage": null
    },
    "discounts": [
      {
        "id": "id7",
        "value": 30.59,
        "discount_type": "discount_type5",
        "status": "status9",
        "created_at": "2016-03-13T12:52:32.123Z",
        "cycles": null,
        "deleted_at": null,
        "description": null,
        "subscription": null,
        "subscription_item": null
      },
      {
        "id": "id8",
        "value": 30.6,
        "discount_type": "discount_type6",
        "status": "status0",
        "created_at": "2016-03-13T12:52:32.123Z",
        "cycles": null,
        "deleted_at": null,
        "description": null,
        "subscription": null,
        "subscription_item": null
      }
    ],
    "increments": [
      null,
      null
    ],
    "subscription": null,
    "name": "name6",
    "quantity": null,
    "cycles": null,
    "deleted_at": null
  },
  "code": null,
  "group": null,
  "amount": null
}
```

