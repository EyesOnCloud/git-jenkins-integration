from main import hello

def test_hello():
    result = hello()
    if result == "Hello, Jenkins!":
        print("Test passed: Hello, Jenkins!")
    else:
        print(f"Test failed: Expected 'Hello, Jenkins!' but got '{result}'")

if __name__ == '__main__':
    test_hello()

