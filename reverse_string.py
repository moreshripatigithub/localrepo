def reverse_string(text: str) -> str:
    return text[::-1]


if __name__ == "__main__":
    value = input("Enter a string: ")
    print(reverse_string(value))