from libgen_api import LibgenSearch
from sagasu_source.book.book import Book
from tqdm import tqdm

def get_libgen_is_book_from_title(search_name: str, filetype: str):
    libgen_progress_bar = tqdm(total=100, position=0, desc='Retrieve from Libgen.Is')
    s = LibgenSearch()
    results = s.search_title_filtered(search_name, {"Extension": filetype}) if filetype != '' else s.search_title(search_name)
    libgen_progress_bar.update(33)
    libgen_progress_bar.set_description("Convert Libgen result to book list")
    book_list = Book.convert_libgen_result_to_book_list(results)
    libgen_progress_bar.update(100)
    libgen_progress_bar.set_description("Convert Libgen result to book list (done)")
    return book_list

def libgen_is_worker(queue, search_name, filetype):
    book_list = get_libgen_is_book_from_title(search_name, filetype)
    queue.put(book_list)