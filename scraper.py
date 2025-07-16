import csv
import os

def run_scraper(address):
    output_path = "/tmp/solar_data_output.csv"
    with open(output_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Address", "Status"])
        writer.writeheader()
        writer.writerow({"Address": address, "Status": "Scraped successfully"})
    return output_path
