import time

import arrow
import requests
from bs4 import BeautifulSoup
from casemgr.helpers.generic import convert_currency_to_decimal, get_browser
from casemgr.models import Booking
from lxml import html
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def write_to_db(content):
    """ """
    html_soup = BeautifulSoup(content, "html.parser")
    table = html_soup.find_all("table")[0]

    # Extract data rows
    for row in table.find_all("tr"):
        data_row = [data.text.strip() for data in row.find_all("td")]
        if data_row:
            data = {
                "inmate_name": data_row[0],
                "booking_id": data_row[1],
                "status": data_row[2],
                "bondable": data_row[3],
                "total_bond": convert_currency_to_decimal(data_row[4]),
            }
            _, is_new =Booking.objects.get_or_create(booking_id=data_row[1], defaults=data)
            if is_new:
                get_booking_details(data_row[1])


def get_roster():
    """ """
    url = "https://cp.spokanecounty.org/detentionservices/inmateroster.aspx"
    table_id = "tblInmateRoster"
    browser = get_browser()
    browser.implicitly_wait(0.5)
    browser.get(url)
    count = 1
    while True:
        print(f"getting data from page {count}")
        # Locate the "Next" button
        next_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div/div[6]/div/div[2]/div[2]/a[3]"))
        )

        # Check if the "ui-disable" class is present in the "Next" button
        if "ui-state-disable" in next_button.get_attribute("class"):
            # If the "ui-disable" class is present, break out of the loop
            break

        data = browser.find_element(By.ID, table_id)  # .get_attribute("content")
        content = data.get_attribute("outerHTML")
        write_to_db(content)

        # Click the "Next" button
        next_button.click()
        count += 1

    time.sleep(2)
    browser.quit()


def get_booking_details(booking_id):
    url = f"https://cp.spokanecounty.org/detentionservices/detail2.aspx?sysid={booking_id}"

    # browser = get_browser()
    # browser.implicitly_wait(0.1)
    # browser.get(url)
    # content = browser.page_source
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    root = html.fromstring(str(soup))
    intakedate_xpath = "/html/body/div/div[4]/text()"
    county_id_xpath = "/html/body/div/div[3]/div[2]/text()"
    # case_xpath = "/html/body/div/div[6]/h2/text()"

    print("TEST", root.xpath(intakedate_xpath)[0])
    intake_date = arrow.get(root.xpath(intakedate_xpath)[0].strip(), "M/D/YYYY [at] h:mm A").datetime
    county_id = root.xpath(county_id_xpath)[0].strip()
    # print("TEST: ", root.xpath(case_xpath)[0])
    booking = Booking.objects.get_object_or_none(booking_id=booking_id)
    if booking:
        booking.update(intake_date=intake_date, county_id=county_id)
