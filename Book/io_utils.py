
def save_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data + "\n")


def append_to_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data + '\n')


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("Файл не существует.")
        return ""


if __name__ == "__main__":
    save_to_file("test.txt", "Hello world!")
    append_to_file("test.txt", "Hello again!")
    print(read_file("test.txt"))