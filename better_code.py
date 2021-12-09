def fibonacci_generator(length=10):
     """Takes in length, return the fibonnacci sequence with given length."""
     sequence = [0, 1]
     for value in range(2, length):
         sequence.append(sequence[value-1] + sequence[value-2])
     return sequence

    
length = input("Please give a lenght of the desired sequence: ")
try:
    length = int(length)
    print(fibonacci_generator(length))
except ValueError:
    # Handle the exception
    print("That is not an integer number.")
