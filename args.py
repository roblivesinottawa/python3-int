def greeting(*args):
    """*args allows for the passing of an unspecified numbers of arguments"""
    for arg in args:
        print(f"hello, {arg}")


greeting("Rob", "Vick", "Beth", "John")
