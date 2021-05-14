def person_data(**kwargs):
    """kwargs allows for the passing of multiple keyworded arguments"""
    print(f"Data type of argument: {type(kwargs)}")

    for k, v in kwargs.items():
        print(f"{k}: {v}")


person_data(firstname="Steve", lastname="Rogers", age=96, country="USA")
