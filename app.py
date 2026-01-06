import requests
import os

def main():
    # خواندن لینک‌ها از سکرت
    raw_links = os.getenv("SOURCE_LINKS", "")
    links = [l.strip() for l in raw_links.split(",") if l.strip()]
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    all_content = []

    for url in links:
        print(f"Fetching: {url}")
        try:
            res = requests.get(url, headers=headers, timeout=25)
            if res.status_code == 200:
                all_content.append(f"--- SOURCE: {url} ---\n{res.text.strip()}\n")
        except:
            print(f"Failed to fetch {url}")

    # ذخیره در فایل
    with open("archive.log", "w", encoding="utf-8") as f:
        f.write("\n".join(all_content))

if __name__ == "__main__":
    main()
