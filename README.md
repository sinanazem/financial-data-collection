
# Financial Data Collection Projects
<img src="https://images.dowjones.com/wp-content/uploads/sites/3/2022/01/27001343/Primer_sentiment_blog_website_1440x420.png">

This repository contains three Python scripts for collecting financial data from various sources.<br><br>
**The scripts are:**

1. **Earning Call Transcript Crawler**: This script uses BeautifulSoup and Selenium to crawl the earnings call transcripts of companies. The transcripts are retrieved using the Alpha Vantage API. The script is designed to retrieve the latest transcript available for a given company.

2. **SEC Edgar Downloader**: This script uses the SEC Edgar API to download filings from the Securities and Exchange Commission's Edgar system. The script can be used to download filings for any company that has filed with the SEC.

3. **Prospectus and Reports Collector**: This script downloads prospectuses and reports for a given set of companies. The script is designed to download documents from the Capital Group and Morgan Stanley websites.

## Dependencies
**The scripts require the following dependencies to be installed:**
- Python 3.9: The scripts are written in Python 3 and require it to be installed on your system.
- BeautifulSoup 4: This is a Python library used for parsing HTML and XML documents. It is used in the earning call transcript crawler and the prospectus and reports collector scripts.
- Selenium: This is a Python library used for automating web browsers. It is used in the earning call transcript crawler script to interact with the Alpha Vantage API website.
- Requests: This is a Python library used for sending HTTP requests. It is used in the SEC Edgar downloader and the prospectus and reports collector scripts to download documents.

## License
This repository is licensed under the MIT license. See the LICENSE file for more details.

## Acknowledgments
- Alpha Vantage for providing the earnings call transcripts API.
- SEC Edgar for providing the SEC filings API.
- Capital Group and Morgan Stanley for providing access to their prospectuses and reports.
