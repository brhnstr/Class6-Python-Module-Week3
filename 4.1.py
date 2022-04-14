def input_function():
    start,end=[int(input('please enter a number'))for _ in range(2)]
    if start> end:
        return end,start
    else:
        return start,end

                
