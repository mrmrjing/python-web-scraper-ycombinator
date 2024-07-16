# Libraries needed: 
#   - requests for making HTTP requests
#   - BeautifulSoup for parsing HTML
#   - smtplib for sending emails
#   - TaskScheduler for scheduling tasks (Cron jobs)

import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import schedule
import time

def fetch_news():
    url = 'https://news.ycombinator.com/' 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Hacker News titles are within 'a.storylink' tags
    news_items = soup.find_all('a', class_='storylink')
    news_content = []
    for item in news_items:
        title = item.text
        link = item['href']
        news_content.append(f"{title}\n{link}\n\n")
    return news_content

def send_email(content):
    email_address = 'your-email@example.com'  # Change to your email
    email_password = 'your-password'  # Change to your password

    msg = EmailMessage()
    msg.set_content('Latest News Update:\n\n' + ''.join(content))
    msg['Subject'] = 'Daily News Update'
    msg['From'] = email_address
    msg['To'] = email_address

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Change SMTP details
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

def job():
    news = fetch_news()
    if news:
        send_email(news)
    else:
        print("No new news found.")

# Schedule to run the job every day at 10am
schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

