from bs4 import BeautifulSoup
import requests
import time

print("Put skill that you are not familiar with: ")
unfamiliar_skill = input('>')
print(F"Filtering out {unfamiliar_skill}")
unfamiliar_skill = unfamiliar_skill.lower()

def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
    for job in jobs:
        job_d = job.find("span", class_="sim-posted")
        job_date = job_d.find("span", class_=None).text
        if "few" in job_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            skills_l = skills.lower()
            more_info = job.header.h2.a['href']   
            if unfamiliar_skill not in skills_l:  
                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"More Info: {more_info}")
                print("")

if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)