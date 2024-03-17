import time

def evaluate_test_cases(the_func, test_cases):
    for test_case_num, test in enumerate(test_cases):
        print(f'TEST CASE #{test_case_num}')
        print(f'{10*"-"}')
        print(f"Input:\n{test['inputs']}")
        print(f'{10*"-"}')
        print(f"Expected Output:\n{test['output']}")
        start = time.time()
        print(f'{10*"-"}')
        print(f"Actual Output:\n{the_func(test['inputs']['cards'], test['inputs']['query'])}")
        end = time.time()
        execution_time = end - start
        print(f'{10*"-"}')
        print(f"Execution Time:\n{(execution_time*1000000):.2f} ms")

        print(f'{10*"-"}')
        if the_func(test['inputs']['cards'], test['inputs']['query']) == test['output']:
            print(f"Test Result:\n\033[32mPASSED\033[0m")
        else:
            print(f"Test Result:\n\033[31mFAILED\033[0m")
        print(f'{79*"="}')