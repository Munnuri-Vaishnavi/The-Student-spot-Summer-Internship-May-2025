import requests
from bs4 import BeautifulSoup
import webbrowser

# Setup
url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
base_url = "https://en.wikipedia.org"

# Title
print(f"Title: {soup.title.string}")

# Meta description
desc = soup.find("meta", attrs={"name": "description"})
if desc:
    print("\nMeta Description:", desc.attrs.get("content"))

# First paragraph
para = soup.find("p")
if para:
    print("\nFirst Paragraph:\n", para.get_text(strip=True))

# Headings
print("\nHeadings:")
for h in soup.find_all(["h1", "h2", "h3"])[:5]:
    print("-", h.get_text(strip=True))

# Useful Links
print("\nWorking Links:")
count = 0
for a in soup.find_all("a", href=True):
    href = a['href']
    text = a.get_text(strip=True)

    if not href or href.startswith("#") or not text:
        continue

    if href.startswith("/"):
        full_url = base_url + href
    elif href.startswith("http"):
        full_url = href
    else:
        continue

    print(f"{text} -> {full_url}")
    count += 1
    if count == 5:
        break

# List Items
print("\nList Items:")
for li in soup.find_all("li")[:5]:
    print("-", li.get_text(strip=True))

# Table Rows
print("\nFirst Table Rows:")
table = soup.find("table")
if table:
    rows = table.find_all("tr")[:3]
    for row in rows:
        cells = row.find_all(["td", "th"])
        line = " | ".join(cell.get_text(strip=True) for cell in cells)
        print(line)
else:
    print("No table found.")

# Forms
forms = soup.find_all("form")
if not forms:
    print("\nNo forms found.")
else:
    for form in forms:
        print(f"\nForm action: {form.attrs.get('action')}")
        for inp in form.find_all("input"):
            print(f"Input name: {inp.attrs.get('name')} | type: {inp.attrs.get('type')}")

# Images - open first 2 in browser
print("\nOpening First 2 Images in Browser:")
images = soup.find_all("img")
for img in images[:2]:
    src = img.get("src")
    if src:
        if src.startswith("//"):
            img_url = "https:" + src
        elif src.startswith("/"):
            img_url = base_url + src
        else:
            img_url = src
        print("Opening:", img_url)
        webbrowser.open(img_url)
