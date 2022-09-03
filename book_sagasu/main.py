import sys,getopt
from tqdm import tqdm
from sagasu_source.utils.write_to_csv import write_to_csv
from sagasu_source.utils.run_in_parallel import runInParallel

DEFAULT_OUTPUT_FILE_NAME='output'

def parse_args(argv):
    bookname = ''
    filetype = ''
    output_file = ''
    try:
        opts, _ = getopt.getopt(argv,"hb:t:o",["bookname=","filetype=", "output="])
    except getopt.GetoptError:
        print("main.py -b <book name> -t <file type>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("main.py -b <book name> -t <file type> -o <output file>")
            sys.exit()
        elif opt in ("-b", "--bookname"):
            bookname = arg
        elif opt in ("-t", "--filetype"):
            filetype = arg
        elif opt in ("-o", "--output"):
            output_file = arg
    if bookname == '' or filetype == '':
        print("main.py -b <book name> -t <file type>")
        sys.exit(2)
    if output_file == '':
        output_file = DEFAULT_OUTPUT_FILE_NAME
    return bookname,filetype,output_file
    

def main(argv):
    bookname,filetype,output_file = parse_args(argv)
    #print(get_libgen_is_book_from_title(bookname,filetype))
    booklist = runInParallel(bookname,filetype)
    write_to_csv_progess_bar = tqdm(total=100, position=2, desc='Found ' + str(len(booklist)) + ' books, writing to ' + output_file + '.csv')
    write_to_csv(output_filename=output_file,book_list=booklist)
    write_to_csv_progess_bar.update(100)
    write_to_csv_progess_bar.set_description('wrote ' + str(len(booklist)) + ' books to ' + output_file + '.csv (done)')
if __name__ == "__main__":
    main(sys.argv[1:])