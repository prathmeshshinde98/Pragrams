from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import smtplib
import os

def sendmail(prices):
    # Clean the prices since ASCII won't recognize Rupee sign (₹), which has a Unicode code point of \u20b9
    clean_price = [s[2:] for s in prices]
    print(clean_price)
    username = os.environ.get('OUTLOOK_USER')
    password = os.environ.get('OUTLOOK_PASSWORD')
    # Establish the connection with outlook server using SMTP module
    with smtplib.SMTP('smtp.outlook.com', 587) as smtp:
        # # Unencrypted ping to server
        # smtp.ehlo()
        # Encrypts further communication
        smtp.starttls()
        # Encrypted ping to server
        smtp.ehlo()
        # Log in details should be put in config file
        smtp.login(username, password)

        # Mail Subject and Body
        subject = 'SkyScanner price check '
        body = f'Top 5 lowest prices are {clean_price}'
        msg = f'Subject: {subject}\n\n {body}'

        # Send mail
        smtp.sendmail('possumtree452@hotmail.com', 'prathmeshshinde1998@gmail.com', msg)


if __name__ == "__main__":
    # Set up Chrome options
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode (without a GUI)

    # Specify the path to your chromedriver
    service = Service('P:\\Programs\\PySpark_Programs\\chromedriver.exe')

    # Create a new instance of the Chrome driver
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    driver = webdriver.Chrome(service=service)
    # Go to the page that requires JavaScript
    url = 'https://www.skyscanner.co.in/transport/flights/pnq/blr/240818/config/15466-2408181730--30643-0-10002-2408181910?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false'
    driver.get(url)

    # Allow time for JavaScript to execute
    time.sleep(10)

    # Get the page source (the rendered HTML after JavaScript execution)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    # Optionally, interact with elements
    element = soup.find_all('span', class_='BpkText_bpk-text__ODgwN BpkText_bpk-text--heading-4__Y2VlY', limit=5)

    price_array = []
    for i in element:
        price_array.append(i.text)
    print(price_array)
    sendmail(price_array)
    # Clean up and close the browser
    driver.quit()
