import os

# Simplest python code. Ever.
print("Hello world!")

# Access test secret variable
test = os.environ['TEST_SECRET']
print("Your secret is", test)
