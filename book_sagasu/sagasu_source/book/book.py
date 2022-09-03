from typing import Any
from libgen_api import LibgenSearch

class Book:

    title = ''
    author = ''
    extension = ''
    download_links = ['']


    def __init__(self, title, author, extension, download_links):
        self.title = title
        self.author = author
        self.extension = extension
        self.download_links = download_links
    
    def convert_libgen_result_to_book_list(results: list[dict[str, Any]]):
        return_list = []
        for result in results:
            s = LibgenSearch()
            download_links = s.resolve_download_links(result)
            return_list.append(Book(title=result.get('Title'),author=result.get('Author'),extension=result.get('Extension'), download_links=[download_links.get('GET'),download_links.get('Cloudflare'),download_links.get('IPFS.io')]))
        return return_list

