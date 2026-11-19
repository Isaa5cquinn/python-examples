
# Python Examples
# A collection of beginner-friendly utility functions.

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def count_words(text):
    return len(text.split())


def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def find_largest(numbers):
    if not numbers:
        return None
    return max(numbers)


if __name__ == "__main__":
    values = [10, 20, 30, 40]

    print("Average:", calculate_average(values))
    print("Word count:", count_words("Learn Python every day"))
    print("Palindrome:", is_palindrome("level"))
    print("Largest number:", find_largest(values))
