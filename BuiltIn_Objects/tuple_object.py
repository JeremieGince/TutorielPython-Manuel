if __name__ == '__main__':
    my_tuple: tuple = ("kevin", "Alphonse", "Benjamain", "Moutarde")

    print(my_tuple[0])
    print(my_tuple[-1])

    print("Moutarde" in my_tuple)
    print("Ketchup" in my_tuple)

    One_item_in_parentheses = (17.3)
    One_item_tuple = (17.3, )  # Notice the comma ','

    print(type(One_item_in_parentheses))
    print(type(One_item_tuple))

    Concat_tuple = my_tuple + One_item_tuple
    print(Concat_tuple)

    simple_list: list = [1, 2, 3, 4, 5]
    simple_tuple: tuple = tuple(simple_list)
    print(type(simple_tuple))
