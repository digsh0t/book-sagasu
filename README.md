# Book Sagasu
A small program that use multi processing technique to find books and their download links from multiple book sources as fast as possible.

# Search source
Currently, the script support finding books on [libgen.is](https://libgen.is) and [dtv-ebook.com](https://www.dtv-ebook.com). More will be supported in the future.

# Setting up

The script can be downloaded and set up using the commands below

```
git clone https://github.com/wintltr/book-sagasu.git
cd book-sagasu
pip install -r requirements.txt
cd book_sagasu
python book-sagasu.py -h
```

# Running BS

Use `python book-sagasu.py -h` to see all the available parameters the script can take

## Book Name

Obviously, this script requires a book name, it can be a vietnamese (i.e "minh niệm") or english

```
python book-sagasu.py -b "minh niệm"
```

## File type

The file type of the book, the script will only returns book with the same file type specified.

Valid file types are "pdf","epub","azw3"

```
python book-sagasu.py -b "minh niệm" -t "azw3"
```

## Output file name

Specify the output csv file name

```
python book-sagasu.py -b "ocd" -t "epub" -o "result"
```
## Sample output result

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/48349230/188273670-1c0de2f4-2dd8-4b4c-90b5-35ae42ab3a1e.png">

# Ongoing problem
Currently, the script sometimes take longer than usual to search for books, it may be due to sites hanging connection. Im trying my best to find the best time to stop the connection.
