x = 5

# assert x>=10, "x is not greater than or equal to 10"
# if the assertion is false, the program will raise an AssertionError with the given
# statement "x is not greater than or equal to 10"

try:
    # x = x/0
    assert x>=5, "x is not greater than or equal to 10"
except AssertionError as e:
    print(e)    # this will print the error message "x is not greater than or equal to 10"
    
except Exception as e:  # this will catch any other exception that is not an AssertionError
    print(e) 
else:
    print("Runs if no exception is raised")
finally:
    print("This will always execute")
    
# custom error class

class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test(x):
    if x < 10:
        raise ValueTooSmallError("x is too small")
    try:
        if x > 10:
            raise ValueTooLargeError("x is too large", x)
    except ValueTooLargeError as e:
        print(f"test failed with '{e.message}' on receiving value {e.value}")

print(test(11)) # this will raise a ValueTooSmallError exception