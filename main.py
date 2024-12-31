from bs4 import BeautifulSoup
import requests
import pypub

file = open("links.txt", "r")

links_list = [line.strip("\n") for line in file]

my_epub = pypub.Epub("My EPUB Title")

def remove_tags(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['li']):
        data.decompose()

    return ' '.join(soup.strings)

for i in range(0, len(links_list)):
    page = requests.get(links_list[i])
    chapter_html = remove_tags(page.content)
    chapter = pypub.create_chapter_from_text(chapter_html, title=f"Chapter {i + 1}")
    my_epub.add_chapter(chapter)

my_epub.create("./My Epub.epub")