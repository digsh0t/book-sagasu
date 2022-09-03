from multiprocessing import Process, Queue
from sagasu_source.dtv_ebook.dtv_ebook import dtv_ebook_worker
from sagasu_source.libgen_is.libgen_is import libgen_is_worker

def runInParallel(bookname,filetype):
    queue = Queue()
    book_list = []
    proc = []
    fns = (
            libgen_is_worker, 
            dtv_ebook_worker,
    )
    for fn in fns:
        p = Process(target=fn, args=(queue, bookname, filetype))
        p.start()
        proc.append(p)
    for p in proc:
        ret = queue.get()
        #Ret can be None, check here
        if ret:
            book_list += ret
    for p in proc:
        p.join()
    return book_list