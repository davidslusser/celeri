import re
from decimal import Decimal

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def convert_currency_to_decimal(currency_string):
    """
    Converts a string representing US currency to a Decimal.

    Args:
      currency_string: A string representing US currency, such as "$1,234.56".

    Returns:
      A Decimal object representing the numerical value of the currency.
    """

    # Remove any leading or trailing whitespace.
    currency_string = currency_string.strip()

    # Remove any currency symbol.
    currency_string = re.sub(r"^\$", "", currency_string)

    # Replace commas with empty strings.
    currency_string = currency_string.replace(",", "")

    # Try converting the string to a float.
    try:
        return Decimal(currency_string)
    except ValueError:
        raise ValueError(f"Invalid currency string: {currency_string}")


def get_browser():
    """_summary_

    Returns:
        _type_: _description_
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    web_driver_path = "/home/david/projects/celeri/tmp/chromedriver-linux64/chromedriver"
    webdriver_service = Service(web_driver_path)
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    return browser
