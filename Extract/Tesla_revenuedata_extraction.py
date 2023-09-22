import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape Tesla revenue data
url_tesla_revenue = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

# Send an HTTP GET request to the URL
response = requests.get(url_tesla_revenue)

if response.status_code == 200:
    # Parse the HTML content
    html_data = response.text

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_data, "html.parser")

    # Find the table containing Tesla revenue data
    tesla_revenue_table = soup.find_all("table")[0]

    # Read the table into a DataFrame
    tesla_revenue = pd.read_html(str(tesla_revenue_table))[0]

    # Rename columns
    tesla_revenue.columns = ["Date", "Revenue"]

    # Remove unnecessary characters and convert 'Revenue' column to float
    tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(',', '').str.replace('$', '').astype(float)

    # Drop rows with missing values
    tesla_revenue.dropna(inplace=True)

    # Display the last five rows of the tesla_revenue dataframe
    print(tesla_revenue.tail())
else:
    print("Failed to retrieve the webpage.")
