import csv

from bs4 import BeautifulSoup
from casemgr.models import Booking


def html2csv(content, filename="output_1.csv"):
    """ """
    html_soup = BeautifulSoup(content, "html.parser")
    table = html_soup.find_all("table")[0]
    # Initialize a list to store rows
    rows = []

    # Extract header row
    header_row = [header.text.strip() for header in table.find_all("th")]
    rows.append(header_row)

    # Extract data rows
    for row in table.find_all("tr"):
        data_row = [data.text.strip() for data in row.find_all("td")]
        if data_row:  # Ignore header row
            rows.append(data_row)

    # Write data to CSV file
    csv_filename = filename
    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)

    print(f"Data has been written to {csv_filename}")


def get_roster():
    """ """
    with open("/home/david/projects/celeri/django_project/test_capture/roster.html", "r") as f:
        content = f.read()

    html_soup = BeautifulSoup(content, "html.parser")
    table = html_soup.find_all("table")[0]
    # Initialize a list to store rows
    rows = []

    # Extract header row
    header_row = [header.text.strip() for header in table.find_all("th")]
    rows.append(header_row)

    # Extract data rows
    for row in table.find_all("tr"):
        data_row = [data.text.strip() for data in row.find_all("td")]
        if data_row:  # Ignore header row
            # inmate_name = data_row[0]
            # booking_id = data_row[1]
            # status = data_row[2]
            # bondable = data_row[3]
            # total_bond = data_row[3]
            # print("TEST: ", data_row[1])
            data = {"inmate_name": data_row[0], "booking_id": data_row[1], "status": data_row[2]}
            # print('TEST: ', data)
            Booking.objects.get_or_create(booking_id=data_row[1], defaults=data)
    # html2csv(content, filename="roster.csv")
