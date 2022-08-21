"""
....
"""

# Exception instead of TypeError
# Don't extend from BaseException
class RuntimeErrorWithCode(TypeError):
    """Exception raised when a specific error code is needed."""
    def __init__(self, message, error_code):
        super().__init__(f'Error Code {error_code}: {message}')
        self.error_code = error_code


# raise RuntimeErrorWithCode('OUCH! An error happened.', 500)

# print('''Hello
# How are you?''')

err = RuntimeErrorWithCode('OUCH! An error happened.', 500)
print(err.__doc__)
