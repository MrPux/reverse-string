#   reverse_string("hello")  # Should return "olleh"
def reverse_string(string):
    return ''.join([i for i in list(string)[::-1]])

print(reverse_string("hello"))