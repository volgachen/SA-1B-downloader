import requests
import wget
import time
import glob

START_PAGE_NO = 
END_PAGE_NO = 
PAGE_SIZE = 10
HEADERS = {
    "content-type": "application/json",
    "cookie": "<your_cookie_here>",
    #"eagleeye-pappname": "<your_pappname_here>",
    #"eagleeye-sessionid": "<your_sessionid_here>",
    #"eagleeye-traceid": "<your_traceid_here>",
    "user-agent": "<your_user_agent_here>"
}
EXCLUDE_FILENAME = set(glob.glob("sa_00*.tar"))

def download_files(dataset_id):
    global EXCLUDE_FILENAME

    # GET files with pageSize and pageNo to obtain a list of path and size
    files = []
    for page_no in range(START_PAGE_NO, END_PAGE_NO + 1):
        files_url = f"https://opendatalab.com/api/datasets/{dataset_id}/files"
        params = {
            "pageSize": PAGE_SIZE,
            "pageNo": page_no,
            "prefix": "raw",
        }
        response = requests.get(files_url, params=params, headers=HEADERS)
        response.raise_for_status()
        files += response.json()["data"]["list"]

    # For each file, POST size and name in payload to obtain the download url, and download it
    for file in files:
        filename = 'raw/' + file["path"]
        if file["path"] in EXCLUDE_FILENAME:
            print(f"{file['path']} already exists, skip ...")
            continue
        print(f"Downloading {filename}...")
        EXCLUDE_FILENAME.add(filename)
        payload = {
            "size": file["size"],
            "name": filename
        }
        track_url = f"https://opendatalab.com/api/track/datasets/download/{dataset_id}"
        response = requests.post(track_url, json=[payload], headers=HEADERS)
        response.raise_for_status()
        download_url = response.json()["data"][0]["url"]
        start_time = time.time()
        print("URL:", download_url)
        wget.download(download_url)
        end_time = time.time()
        print(f"Time taken to download {filename}: {end_time - start_time:.2f} seconds\n")

download_files(6248)
