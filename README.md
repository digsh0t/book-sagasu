# Book Sagasu
A small program to find books and their download links from multiple book sources.

# Setting up

The script can be downloaded and set up using the commands below

```
git clone https://github.com/wintltr/book-sagasu.git
pip install -r requirements.txt
cd book-sagasu/book_sagasu
python book-sagasu.py -h
```

# Running BS

Use `python3 book-sagasu.py -h ` to see all the available parameters the script can take

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
python book-sagasu.py -b "minh niệm" -t "azw3" -o "result"
```
