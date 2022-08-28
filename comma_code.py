def list_to_string(list):
    return ', '.join(list[:-1]) + ", and " + list[-1] # This function returns a joined list, using the delimiter specified
                                                      # before the method. It goes until the last item, and concatenates
                                                      # the item after ', and'. Will work on all lengths of list.

list1 = ['apples', 'bananas', 'tofu', 'cats']
print(list_to_string(list1))