## TRADITIONAL FOR-LOOPS
squares_one = []

for i in range(5):
    squares_one.append(i**2)
    
print(squares_one)

## LIST-COMPREHENSION

squares_two = [i**2 for i in range(5)]
print(squares_two)


def process_data (data: int | str) -> str:
    if isinstance(data, int):
        return f"Processed number: {data}"
    return f"Processed string: {data}"

print(process_data("string"))
print(process_data(5))

numbers = [1, 2, 3, 4, 5]

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)