# Web Scraping with Selenium AVG Salary in Poland 1950-2022

This repository contains a Python script for web scraping using the Selenium library to extract data from a specific webpage and save it to a CSV file. The script navigates to a URL and extracts various types of content from the page, including text from a `<div>` element, text from a centered `<p>` tag, and text from a table. The extracted data is then saved to a CSV file with proper character encoding.

## Prerequisites

- Python 3.x
- Selenium library
- Edge webdriver executable (ensure it is in your PATH)

## Installation

1. Clone this repository to your local machine or download the script directly.
2. Install the required Python packages using the following command:
   ```bash
   pip install selenium

## Usage
Make sure you have the Edge webdriver executable in your PATH. You can download it from the official Edge WebDriver page: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Update the url variable in the script to the desired URL.

 Run the script using the following command:
 ```
 python web_scraping_script.py
 ```

The script will open a browser window, navigate to the specified URL, and extract the required data.
The extracted data will be saved to a CSV file named zus_data.csv in the same directory as the script.
The script will print a message indicating the location where the data has been saved.
Script Explanation

The script imports the necessary modules from the Selenium library.
It sets up the Edge webdriver, navigates to the specified URL, and finds the desired elements using XPath.
The content of the extracted elements is stored in variables.
The webdriver is closed after the data is extracted.
The extracted content is written to a CSV file using UTF-8-sig encoding to ensure proper character handling.
## Note
Web scraping may be subject to terms of use of the website. Make sure to review and comply with the website's terms and policies before scraping.
Ensure you are respectful of the website's resources and do not overload their server with excessive requests.
## Acknowledgments
This script was created for educational purposes as an example of web scraping using Selenium. It may be further customized and extended to suit specific scraping requirements.

Feel free to contribute to the repository and make improvements!

Happy scraping!
