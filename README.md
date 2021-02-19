
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

Usage

Run the game script:

    python shopping_cart.py

(Adapted from from Professor Rossetti's markdown)