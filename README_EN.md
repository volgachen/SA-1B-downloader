# SA-1B-Downloader

[简体中文](README.md) | English

This script allows for convenient downloading of the SA-1B dataset from opendatalab.com.

Advantages:
- Continuous, unmanned automation of downloads
- Convenient for multiple people to work together and download

## Environment Configuration
`pip install requests wget`

## Download
- Place `sa_download.py` in the directory where you want to store the dataset files, making sure there is enough disk space.
- Open the [OpenDataLab website](https://opendatalab.com/SA-1B/download) in a browser and register/login.
- Press F12 to open the developer panel, go to "Network", and perform a page jump at the bottom of the webpage to view the request header. Copy the `cookie` and `user-agent` items to the corresponding lines in the code file. Refer to the following image for operation.
- Determine the number of pages you need to download according to your division of labor (default is 10 lines per page, the same as displayed on the webpage), and fill in `START_PAGE_NO` and `END_PAGE_NO` in the code. The page number starts at index 1 and includes the start and end pages during downloading.
- Run `python sa_download.py` in the storage directory.

![2](https://user-images.githubusercontent.com/34768678/234220708-cadba2f4-bcbd-4bf9-a3f0-5dc7ee2208fe.png)

## Successful Operation Example

![1](https://user-images.githubusercontent.com/34768678/234219130-d68ef830-ee07-4a3d-8a5a-909a30efd0d3.png)

## Acknowledgement

We thank OpenDataLab to share these files and thank ChatGPT to help me with the script.
