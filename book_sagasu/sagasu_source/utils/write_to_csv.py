import csv

from sagasu_source.book.book import Book

def write_to_csv(output_filename: str, book_list):
    data = []
    header = ['Book name', 'Author', 'Extension', 'Download links']
    for book in book_list:
        data.append([book.title,book.author, book.extension, book.download_links[0]])
        for link in book.download_links[1:]:
            data.append(['','', '', link])

    with open(f'{output_filename}.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)