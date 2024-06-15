# currencyconverter
This Python script serves as a currency converter, allowing users to obtain conversion rates for a specified base currency against multiple other currencies using the FreeCurrencyAPI.

Requirements
Python 3.x
requests library (pip install requests)
Usage
Obtain API Key: Sign up on the FreeCurrencyAPI website to obtain your API key.

Set API Key: Insert your API key into the API_KEY variable within the script.

Run the Script: Execute the script using a Python interpreter.

Input Base Currency: Enter the base currency you wish to convert. To exit the program, type "X" and press Enter.

View Conversion Rates: The script will display the conversion rates for the specified base currency against USD, CAD, EUR, and AUD.

Script Overview
Importing Libraries: The script imports the requests library to handle HTTP requests.

Defining Constants: It sets the API_KEY variable to authenticate requests with the FreeCurrencyAPI. The BASE_URL variable constructs the base URL for API requests, including the API key.

Specifying Target Currencies: The CURRENCIES list contains the currencies against which the base currency will be converted.

Conversion Function: The convert_currency() function takes a base currency as input, constructs the API request URL with the specified base currency and target currencies, sends a GET request to the API, and returns the exchange rate data.

User Interaction Loop: The script utilizes a while loop to continuously prompt the user for input. It breaks the loop when the user enters "X" to quit.

Conversion Process: Within the loop, it calls the convert_currency() function with the user-provided base currency. If successful, it displays the conversion rates for each target currency.

Error Handling
API Request Failure: If the API request fails, the script prints "Invalid currency!" and returns None.

Invalid User Input: If the user enters an invalid currency or the API request fails, the script prompts for re-entry.

Note
Ensure your system has an active internet connection to access the FreeCurrencyAPI.
Use your API key responsibly and adhere to the terms of service provided by FreeCurrencyAPI.
Feel free to customize or integrate this script according to your requirements!