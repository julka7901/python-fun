def specjalnyLoop (iterowana):
    iterator = iter(iterowana)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break
         
specjalnyLoop([1,2,3])