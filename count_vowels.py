def count_vowels(input_string):
    vowels = set('aeiou')
    vowels_list = list(input_string)
    vowels_in_string=[]
    vowels_list_without_duplicates=[]
    final_tuple=()
    length_turple =()
    result= ''
    for c in vowels_list:
        if c in vowels:
            vowels_in_string.append(c)

    for vowel in vowels_in_string: 
        if vowel not in vowels_list_without_duplicates: 
            vowels_list_without_duplicates.append(vowel)
            
    no_duplicates_tuple=tuple(vowels_list_without_duplicates)
    tuple_length =len(no_duplicates_tuple)
    length_turple += (tuple_length,)
    final_tuple=(no_duplicates_tuple) +length_turple
    print(final_tuple)
    
count_vowels("Museveni")

                
    
