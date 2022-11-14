from bs4 import BeautifulSoup
import requests
import csv


url = "https://www.flipkart.com/poco-m4-5g-cool-blue-128-gb/product-reviews/itm1603244ab4f2e?pid=MOBGDRGPUMTED5D5&lid=LSTMOBGDRGPUMTED5D5P1XEJA&marketplace=FLIPKART"
def getDetailsfromReview(allDivs: list):
    output = []
    for i in allDivs:
        reviewDetails = {}
        subsections = i.div.div.div.findAll("div")
        reviewDetails["rating"] = subsections[0].div.get_text().strip()
        reviewDetails["heading"] = subsections[0].p.get_text().strip()
        reviewDetails["text"] = subsections[2].get_text().strip().replace("READ MORE", "")
        output.append(reviewDetails)
    return output


def getReviews(url: str):
    html = requests.get(url).content.decode()
    soup = BeautifulSoup(html, "html.parser")
    containerDiv = soup.find("div")
    cd = containerDiv.div
    allDivs = list(list(list(cd.children)[2].div.div.children)[1].children)[4:-1]
    return getDetailsfromReview(allDivs)

def writeToCSV(data: list):
    with open("reviews.csv", "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["rating", "heading", "text"])
        writer.writeheader()
        writer.writerows(data)


reviews = getReviews(url)
writeToCSV(reviews)
print("DONE!! check reviews.csv in this folder")


