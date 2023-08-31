from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Edge webdriver (ensure you have the appropriate driver executable in the PATH)
driver = webdriver.Edge()

# Navigate to the URL
url = "https://www.zus.pl/baza-wiedzy/skladki-wskazniki-odsetki/wskazniki/przecietne-wynagrodzenie-w-latach"
driver.get(url)

# Find the desired elements
table_element = driver.find_element(By.XPATH, "//table")
td_elements = table_element.find_elements(By.XPATH, "//td[contains(@style, 'text-align: center')]")

# Extract and format data from td_elements
data_list = []
for i in range(0, len(td_elements), 3):
    year = td_elements[i].text
    annual_salary = td_elements[i + 1].text
    salary_x_12 = td_elements[i + 2].text

    if int(year) >= 1995:
        annual_salary = annual_salary.replace(" ", "").replace(",", ".")
        salary_x_12 = salary_x_12.replace(" ", "").replace(",", ".")

    data_list.append([year, annual_salary, salary_x_12])

# Close the webdriver
driver.quit()

# Write the data to a CSV file with proper character encoding
csv_filename = "zus_data.csv"

with open(csv_filename, mode='w', encoding='utf-8-sig') as csv_file:
    csv_file.write("Year,Annual Salary,Salary x 12 months\n")
    for data in data_list:
        csv_file.write(",".join(data) + "\n")

print(f"Data saved to {csv_filename}")
