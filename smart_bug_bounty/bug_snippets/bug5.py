def add_item(item, collection=[]):
    """
    Add an item and return the updated collection.
    """
    collection.append(item)
    return collection


def main():
    first = add_item("apple")
    second = add_item("banana")

    print("First:", first)
    print("Second:", second)


if __name__ == "__main__":
    main()
