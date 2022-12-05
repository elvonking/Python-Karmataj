# scraping the real_python_dot_com fake jobs website
# you need requests for this
# you also need beautiful soup
# pandas to output the results into a dataframe

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# checkout the result, a bunch of html code for the page
# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

# find name by id
results = soup.find(id = "ResultsContainer")

# print(results.prettify())

# next we find items by class
job_elements = results.find_all("div", class_="card-content")

# let's see what we get
# for job_element in job_elements:
#     print(job_element, end="\n"*2)

# make that more useful
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()

# so that gets us every job, not just dev jobs
# let's fix that with some filtering
# let's fetch only python jobs

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
# what do we get
# print(len(python_jobs))
# print(python_jobs)
# 10 python jobs and nothing else, printing the objects throws an error

# let's now get the elements from the appropriate parent tag for the target h2 tag
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# print(python_job_elements)

# now we can see the python jobs details
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    # links = job_element.find_all("a")
    # for link in links:
    #     link_url = link["href"]
    #     print(f"Apply here: {link_url}\n")
    # this returns two links, one for learn, second for apply

    # we can find the appropriate (apply) link better
    link_url = job_element.find_all("a")[1]["href"]
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f"Apply here: {link_url}\n")
    print()

# you can store the results you get in a pandas dataframe for further analysis
data_dict = {
    "title": title_element,
    "company": company_element,
    "location": location_element,
    "link": link_url
}

# needs to be fixed to show all the jobs, not one repeatedly
df = pd.DataFrame(data_dict, index=np.arange(len(python_job_elements)))
print(df)