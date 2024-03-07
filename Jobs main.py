import pandas as pd
import requests
from bs4 import BeautifulSoup


job_design = []
Company = []
Experience = []
Location = []
More_loc = []
job_area = []

url = "https://www.shine.com/job-search/data-analyst-jobs-in-kerala?q=data-analyst&loc=Kerala"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
# box = soup.find("div", {"class": "jsrpcomponent_jsrp_leftPanel__2nm3w jsrp_leftPanel"})

for i in range(1,6):
    np = soup.find("a", {"title": "Next"}).get("href")
    cmp = "https://www.shine.com/job-search/" + np

    url = cmp
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    job_name = soup.find_all("div", {"itemprop": "itemListElement"})
    for job in job_name:
        tag = job.find("a", class_=False)
        job_des = tag.text
        job_design.append(job_des)
        print(len(job_design))

    job_comp = soup.find_all("div", {"class": "jobCard_jobCard_cName__mYnow"})
    for c in job_comp:
        comp = c.text
        Company.append(comp)
        print(len(Company))

    job_exp = soup.find_all("div", {"class": "jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"})
    for e in job_exp:
        ex = e.text
        Experience.append(ex)
        print(len(Experience))

    job_loc = soup.find_all("div", {"class": "jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"})
    for loc in job_loc:
        locate = loc.contents[0].strip()
        Location.append(locate)
        print(len(Location))

    job_locs = soup.find_all("div", {"class": "more_info_text arrow-box down_arrow arrow-right"})
    for lo in job_locs:
        locs = lo.text
        More_loc.append(locs)
        print(len(More_loc))

    work = soup.find_all("ul", {"class": "jobCard_jobCard_jobDetail__jD82J"})
    for w_like in work:
        w = w_like.find("li").text
        job_area.append(w)
        print(len(job_area))

df = pd.DataFrame({"Job_name": job_design, "Company": Company, "Experience": Experience, "Location": Location,
                   "More_location": More_loc, "Working type": job_area})
# print(df)


df.to_csv("shine jobs Analyst ker.csv")
