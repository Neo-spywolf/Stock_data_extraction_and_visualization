# URL to scrape GameStop revenue data
url_gme_revenue = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

# Send an HTTP GET request to the URL
response = requests.get(url_gme_revenue)

if response.status_code == 200:
    # Parse the HTML content
    html_data = response.text

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_data, "html.parser")

    # Find the table containing GameStop revenue data
    gme_revenue_table = soup.find_all("table")[0]

    # Read the table into a DataFrame
    gme_revenue = pd.read_html(str(gme_revenue_table))[0]

    # Rename columns
    gme_revenue.columns = ["Date", "Revenue"]

    # Remove unnecessary characters and convert 'Revenue' column to float
    gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(',', '').str.replace('$', '').astype(float)

    # Display the last five rows of the gme_revenue dataframe
    print(gme_revenue.tail())
else:
    print("Failed to retrieve the webpage.")

