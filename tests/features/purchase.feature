Feature: Purchase an item
    Purchase an item

    Scenario: Complete the purchase
        Given the user is in the home page
        When the user logins as "standard user"
        And the user selects an item
        And the user clicks in the cart button
        Then the user sees the item in the cart matches the one selected
        When the user clicks in the checkout button
        And the user inputs "Daniel" in the first name field
        And the user inputs "Giraldo" in the last name field
        And the user inputs "050012" in the zip field
        And the user clicks in the continue button
        And the user clicks in the finish button
        Then validate the text order is completed succesfully