
Shopping Cart Project

A tool that allows a human user to utilize a modern checkout system for a grocery store.

Prerequisites

Anaconda 3.7+ Python 3.7+ Pip

Installation

Navigate to the repository from the command line (subsequent commands assume you are running them from the local repository's root directory) by using the following command:

    cd shopping-cart
(Use cd ~/Desktop/shopping-cart  if the repository is stored in the desktop)

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

    conda create -n shopping-env python=3.8 
    conda activate shopping-env

From inside the virtual environment, install package dependencies:

    pip install -r requirements.txt

    pip install sendgrid


Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your municipality's sales tax rate and to change the default sales tax rate of 8.75% (replace ".0875" with the correct sales tax rate):

    TAX_RATE = .0875

To set up emailing receipt capabilities, first, sign up for a SendGrid account, then follow the instructions to complete your "Single Sender Verification", clicking the link in a confirmation email to verify your account.

Then create a SendGrid API Key with "full access" permissions. Store the API Key value in the ".env" file (replace " " with the correct API Key value):

    SENDGRID_API_KEY = " "

Update the contents of the ".env" file to specify the email address of the sender. This should be the same email address as the single sender address associated with the SendGrid account:
    
    SENDER_ADDRESS = "tiffanyandgro@gmail.com"

Navigate to https://sendgrid.com/dynamic_templates and press the "Create Template" button. Give it a name like "example-receipt", and click "Save". At this time, you should see your template's unique identifier (e.g. "d-b902ae61c68f40dbbd1103187a9736f0"). Copy this value and store it in an environment variable in the ".env" file:

    SENDGRID_TEMPLATE_ID = "d-b902ae61c68f40dbbd1103187a9736f0"

Back in the SendGrid platform, click "Add Version" to create a new version of a "Blank Template" and select the "Code Editor" as your desired editing mechanism.

The following can be used as the HTML for the Code template:

    <img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

    <h3>Hello this is your receipt</h3>

    <p>Date: {{human_friendly_timestamp}}</p>

    <ul>
    {{#each products}}
        <li>You ordered: {{this.name}} {{this.price}}</li>
    {{/each}}
    </ul>

    <p>Total: {{total_price_usd}}</p>

The following can be used for the Test Data to populate the template:

    {
    "total_price_usd": "$99.99",
    "human_friendly_timestamp": "July 4th, 2099 10:00 AM",
    "products":[
        {"id": 100, "name": "Product 100", "price": 2.00},
        {"id": 200, "name": "Product 200", "price": 2.00},
        {"id": 300, "name": "Product 300", "price": 2.00},
        {"id": 200, "name": "Product 200", "price": 2.00},
        {"id": 100, "name": "Product 100", "price": 2.00}
        ]
    }

Name and save the template. 

Usage

Run the game script:

    python shopping_cart.py

(Adapted from from Professor Rossetti's markdown)