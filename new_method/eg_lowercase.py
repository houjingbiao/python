
class LowerCaseTuple(tuple):
    def __new__(cls, iterable):
        lower_iterable = (l.lower() for l in iterable)
        return super().__new__(cls, lower_iterable)
def lower_case_example():
    print(LowerCaseTuple(['HELLO', 'MEDIUM']))
def main():
    lower_case_example()
if __name__ == '__main__':
    main()