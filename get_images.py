import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
import json
from google_images_download import google_images_download
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-k', '--keywords', help='delimited list input', type=str, required=True)
parser.add_argument('-l', '--limit', help='delimited list input', type=str, required=True)
parser.add_argument('-o', '--output_directory', help='download images in a specific main directory', type=str, required=False)
args = parser.parse_args()
arguments = vars(args)
response = google_images_download.googleimagesdownload()
response.download(arguments)

