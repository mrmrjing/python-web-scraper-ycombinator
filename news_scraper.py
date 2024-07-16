# Libraries needed: 
#   - requests for making HTTP requests
#   - BeautifulSoup for parsing HTML
#   - smtplib for sending emails
#   - TaskScheduler for scheduling tasks (Cron jobs)

import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
from urllib.parse import urljoin



# Load environment variables from .env file
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))

def fetch_news():
    url = 'https://news.ycombinator.com/' 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.find_all('span', class_='titleline')
    news_content = []
    for item in news_items:
        link_tag = item.find('a') # find the <a> tag within each <span>
        if link_tag: 
            title = link_tag.text
            href = link_tag['href']
            # Check if the URL is relative and make it absolute if needed 
            link = urljoin(url, href)
            news_content.append(f"{title}\n{link}\n\n")
    return news_content

def send_email(content):
    msg = EmailMessage()
    msg.set_content('Latest News Update from Hacker News:\n\n' + ''.join(content))
    msg['Subject'] = 'Hacker News Daily Digest'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

def job():
    news = fetch_news()
    if news:
        send_email(news)
    else:
        print("No new news found.")

if __name__ == "__main__":
    job()
