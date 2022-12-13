
# Application for lean tech

This is the technical exercise proposed by lean tech for the application of Daniel Felipe Giraldo Espinosa
following these steps

- Go to https://www.saucedemo.com/
- Log in to the application with the “standard_user” user.
- Add any product to the cart.
- Get the text value (name of the item – the one red highlighted) of the item you add to the cart. 
- Go to the cart page.
- Validate that the item name text is the same that you got in the previous step
- Click on Checkout.
- Fill in the information and continue to the next page.
- In the “CHECKOUT: OVERVIEW” page, validate that the item name text is the same that you got in the previous step
- Finish the order.
- Validate that you finish the order.
- You can validate that you are at the “CHECKOUT: COMPLETE!” page using that text or another one.

# How to run the test
After cloning the repository please run the following command from the root directory 
```bash
  pipenv install
```

This will install all the dependencies in a virtual environment. Then run the following command
```bash
  pipenv run python -m pytest
```
