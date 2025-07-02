import functools
import shutil
import tempfile
import urllib.request
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup


@dataclass
class ComicData:
    id: int
    title: str
    image_path: str


def get_html_by_id(comic_id: int) -> ComicData | None:
    with requests.get(f"https://xkcd.com/{int(comic_id)}/") as req:
        if req.status_code != 200:
            return None
        html_content = req.text

    return parse_html_content(html_content)


def get_html_by_random():
    with requests.get("https://c.xkcd.com/random/comic/") as req:
        if req.status_code != 200:
            return None

        comic_id: int = int(req.url.strip("/").split("/")[-1])
        html_content = req.text

    comic_data = parse_html_content(html_content)
    if not comic_data:
        return None
    comic_data.id = comic_id
    return comic_data


@functools.cache
def parse_html_content(html: str) -> ComicData | None:
    soup = BeautifulSoup(html, "html.parser")

    title: str = soup.find("meta", attrs={"property": "og:title"})["content"]  # type: ignore
    image_url: str = soup.find("meta", attrs={"property": "og:image"})["content"]  # type: ignore

    # Download image in temporary file.
    response = urllib.request.urlopen(image_url)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    shutil.copyfileobj(response, temp_file)
    return ComicData(0, title, temp_file.name)
