import enum
class Seed(enum.Enum):
    CROSS = 'X'
    NOUGTH = 'O'
    NO_SEED = ' '

def main():   
    print(vector())

def vector():
    A = [''] * 9
    for i in range(9):
        A[i] = Seed.CROSS.value
    return A
main()