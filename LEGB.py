my_string = "Kemal"


# Global ->

def my_func():
    my_string = "James"
    print(my_string)
    # Enclosing

    def my_func_2():
        # Local
        my_string = "Lars"
        print(my_string)

    my_func_2()

my_func()
print(my_string)