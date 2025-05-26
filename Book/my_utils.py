def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def word_count(text):
    return len(text.split())


def shorten(text, max_length):
    return text if len(text) <= max_length else text[:max_length] + "..."


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number)):
        if number % i == 0:
            return False
    return True


def digit_sum(num):
    return sum(int(d) for d in str(num))


def reverse_number(n):
    return int(str(n)[::-1])


if __name__ == "__main__":
    print(is_palindrome("abcba"))
    print(word_count("Hello world!"))
    print(shorten("Hello world!", 10))
    print(is_prime(1))
    print(digit_sum(12345))
    print(reverse_number(12345))