![](https://raw.githubusercontent.com/primer-api/primer-api/main/header.png)

# :rocket: Backend Technical Interview - Pair Programming

At Primer, we're building the last payments API that a merchant will ever need to integrate with. By integrating with Primer a merchant will have access to any payment processor (PSP) they want, as well as other services across the payments stack such as fraud providers.

There are two main stages to processing a payment at checkout, the first is **tokenizing** the card data, and the second is **authorizing** a payment against this token.

One of the big benefits of using Primer is that we have an abstraction on tokenization, which means that a merchant can store card details agnostically and only choose the payment processor at the point of authorization.

# :pear: Format

One of our devs has gone on holiday and left our prototype API incomplete, so we need a proficient developer to come in and clean up what's been left behind - that's you!

All you need to do for now is ensure you can run the project below locally, more details will follow before the interview itself.

Please note, you will be asked to share your screen via Google Meet, so please check you have tested this prior to the interview to ensure you don't run into any system permission issues.

## :crystal_ball: The project

Please make sure you can run the project locally prior to the interview. You should be able to run the service and the tests (which should fail).

### Pre-requisites

In order to run the project you will need to have installed:

- Python 3 (we recommend Python 3.9, but in theory any Python 3 version should be fine)
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
- `make` (optional, but recommended to run the commands in Makefile)

### Setup

Run this the first-time you have set up in order to install the Pipenv virtual environment:

    make setup

### Spin up the API

    make develop

### Run tests

    make test

Please note, the tests should fail initially.
