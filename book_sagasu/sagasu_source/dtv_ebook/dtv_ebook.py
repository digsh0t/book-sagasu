import logging
import re
from tqdm import tqdm
import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from sagasu_source.utils.request_retry_session import requests_retry_session


from sagasu_source.book.book import Book

DTV_EBOOK_SEARCH_ENDPOINT = 'https://www.dtv-ebook.com/tim-kiem.html'

def get_dtv_ebook_link(bookname: str, pbar):
    returned_links = []
    params = {'keyword': bookname}
    try:
        requests_session = requests_retry_session()
        r = requests_session.get(url = DTV_EBOOK_SEARCH_ENDPOINT, params = params)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        pbar.update(100)
        pbar.colour="red"
        pbar.set_description('Get book from dtv_ebook (fail)')
        pbar.close()
        return None, err
  
    soup = BeautifulSoup(r.text, 'html.parser')
    result_divs = soup.find_all("div", {"class": "hide-for-small-only"})
    for div in result_divs:
        book_link = div.a.get('href')
        returned_links.append(book_link)
    return returned_links, None

def get_dtv_ebook_book_from_title(bookname: str, filetype: str):
    dtv_ebook_progess_bar = tqdm(total=100, position=1, desc='Retrieve book page from dtv_ebook')
    return_book_list = []
    result, err = get_dtv_ebook_link(bookname, dtv_ebook_progess_bar)
    if err:
        logging.exception(err)
        return None
    dtv_ebook_progess_bar.update(50)
    dtv_ebook_progess_bar.set_description("Get dtv_ebook book from detail page")
    return_book_list = asyncio.run(get_dtv_ebook_book_detail_page(result,filetype))
    dtv_ebook_progess_bar.update(100)
    dtv_ebook_progess_bar.set_description("Get dtv_ebook book from detail page (done)")
    return return_book_list
    
async def get(url, session):
    try:
        async with session.get(url=url) as response:
            resp = await response.read()
            return resp
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))


async def get_dtv_ebook_book_detail_page(urls, filetype):
    return_book = []
    async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(*[get(url, session) for url in urls])
    for respond_content in ret:
        book = process_detail_page(respond_content, filetype)
        if book:
            return_book.append(book)
    return return_book


def process_detail_page(content, filetype):
    if not content:
        return None
    soup = BeautifulSoup(content, 'html.parser')
    try:
        a_tag = soup.find("a", {"title": filetype.upper()})
        download_link = re.sub('\\r','',a_tag.get('href'))
        a_tag = soup.find("a", {"class": "label success radius"})
        author = a_tag.get('title')
        h2_tag = soup.find("h2", {"class": "ten_san_pham text-center"})
        title = h2_tag.text
        return Book(title, author, extension=filetype, download_links=[download_link])
    except:
        return None

def dtv_ebook_worker(queue, bookname, filetype):
    book_list = get_dtv_ebook_book_from_title(bookname, filetype)
    queue.put(book_list)