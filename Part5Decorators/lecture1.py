# Decorators
def print_hi():
    print(f'Hi there')


# message = print_hi()
message = print_hi
# print(message)
print(message())


def print_m(funct_name):
    print(funct_name())


def message():
    return 'Message Fn'


msg = print_m(message)
print(msg)

# HOC
def first():
    def second():
        return 'Hi'
    return second()

print(first())
