from evaluate_test_cases import evaluate_test_cases

# Step 1. State the problem and identify the inputs and outputs.
#     Problem:
#         WAP to find the position of a given number in a list of numbers sorted in decreasing order.
#     Inputs:
#         cards -> the list of nnmbers arranged in decreasing order.
#         query -> the number whose positoin is to be found.
#     Outputs: 
#         position -> the position of 'query' in 'cards'.
# Step 2. Think of some example inputs and outputs and try to cover all the edge cases.
tests = [
    {
        # The query is anywhere in the list
        'inputs': {
            'cards': [15, 11, 10, 7, 6, 3, 1, 0],
            'query': 1
        },
        'output': 6,
    },
    {
        # The query is the first element
        'inputs': {
            'cards': [15, 11, 10, 7, 6, 3, 1, 0],
            'query': 15
        },
        'output': 0,
    },
    {
        # The query is the last element
        'inputs': {
            'cards': [15, 11, 10, 7, 6, 3, 1, 0],
            'query': 0
        },
        'output': 7,
    },
    {
        # The list contains only one element
        'inputs': {
            'cards': [24],
            'query': 24
        },
        'output': 0,
    },
    {
        # The list does not contain the element
        'inputs': {
            'cards': [15, 11, 10, 7, 6, 3, 1, 0],
            'query': 24
        },
        'output': -1,
    },
    {
        # The list is empty
        'inputs': {
            'cards': [],
            'query': 24
        },
        'output': -1,
    },
    {
        # The list has repeating numbers
        'inputs': {
            'cards': [24, 24, 24, 24, 24, 6, 6, 6, 6, 6, 7 , 3, 2, 1, 0],
            'query': 7
        },
        'output': 10,
    },
    {
        # The list has multiple entries for the query
        'inputs': {
            'cards': [24, 24, 24, 24, 24, 6, 6, 6, 6, 6, 7 , 3, 2, 1, 0],
            'query': 6
        },
        'output': 5,
    },
]

print(tests)
# Step 3. Think of the solution and state it in plane English.
    # 1. create a variable 'position' with value 0.
    # 2. check weather the number at index 'position' in 'cards' equals 'query'.
    # 3. if yes then 'position' is our answer and can be returned from the function.
    # 4. if not then increment the value of 'position' by 1 and repeat steps 2 to 5 till we reach the last element of cards.
    # 5. if the number was not found retrun -1.

def locate_card(cards, query):
    if not cards:
        return -1
    else:
        # Create a variable 'position' with value 0.
        position = 0
        # Setup loop for repetition.
        while True:
            # Check weather the number at index 'position' in 'cards' equals 'query'.
            if cards[position] == query:
                # Answer found return and exit
                return position
            
            # Increment by 1
            position += 1
            
            # Check if the end of the list/array is reached.
            if position == len(cards):
                # Number not found return -1.
                return -1

# Step 4. Implement the soution and test it with the example inputs, fix bugs if any.
evaluate_test_cases(locate_card, tests)

# Step 5. Analyze the algorithm's complexity and indetify inefficiencies, if any.
# Step 6. Apply right technique to overcome the inefficieny and repeat steps 3 to 6.