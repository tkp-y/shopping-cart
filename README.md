
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

From within an active virtual environment, install the sendgrid package:

    pip install sendgrid


Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your municipality's sales tax rate and to change the default sales tax rate of 8.75% (replace ".0875" with the correct sales tax rate):

    TAX_RATE = .0875

To set up emailing receipt capabilities, first, sign up for a SendGrid account, then follow the instructions to complete your "Single Sender Verification", clicking the link in a confirmation email to verify your account.

Then create a SendGrid API Key with "full access" permissions. Store the API Key value in the ".env" file (replace "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" with the correct API Key value):

    SENDGRID_API_KEY = "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"

Update the contents of the ".env" file to specify the email address of the sender. This should be the same email address as the single sender address associated with the SendGrid account:
    
    SENDER_ADDRESS = "tfk15@georgetown.edu"

Navigate to https://sendgrid.com/dynamic_templates and press the "Create Template" button on the top right. Give it a name like "example-receipt", and click "Save". At this time, you should see your template's unique identifier (e.g. "d-fc7da48ed9904f7884f4d882a55c56ec"). Copy this value and store it in an environment variable in the ".env" file:

    SENDGRID_TEMPLATE_ID = "d-fc7da48ed9904f7884f4d882a55c56ec"

Usage

Run the game script:

    python shopping_cart.py

(Adapted from from Professor Rossetti's markdown)