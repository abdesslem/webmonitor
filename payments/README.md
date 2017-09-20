# Payments microservice

The payments microservice use stripe Subscriptions API to handle plans and customers.

## Initial step
To start using Stripe Subscriptions we have to define the diffrents plans

## Use cases
The client can:

- List all the services (plans) availables
- Select and Pay a plan
- Upgrade a Subscription

## Service endpoint

- **GET /services** : Get the list of availables plan
- **POST /services/<serviceId>**: Select a plan

## Checkout endpoint

- **GET /checkout** : Get the invoice
- **POST /checkout**: Pay the invoice

