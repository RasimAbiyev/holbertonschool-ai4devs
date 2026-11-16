def get_last_items(items, n):
    """Return the last n items from a list."""
    if n < 0:
        raise ValueError("n cannot be negative")

    if n == 0:
        return []

    return items[-n:]


if __name__ == "__main__":
    values = [10, 20, 30, 40, 50]
    print(get_last_items(values, 3))
