def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            print(i),
            count += 1
            if count == x:
                break
    except TypeError:
        print "Error: Invalid input list."
    finally:
        print
    return count

