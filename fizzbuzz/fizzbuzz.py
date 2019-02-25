def fizzbuzz(list1,list2):
    if type(list1) is list and type(list2) is list:
        list1_length =len(list1)
        list2_length = len(list2)
        combined_list_length = list1_length + list2_length

        if combined_list_length%3==0:
            return "fizz"
        elif combined_list_length%5==0:
            return "buzz"
        elif (combined_list_length%5==0 and combined_list_length%3==0):
            return "Fizzbuzz"
        else:
            return (combined_list_length)
    else:
        return "one of the entries is not a list"
    
fizzbuzz([1, 2, 3], [1])
    
