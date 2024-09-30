def max_sum(a,n):
    #code here
     # Step 1: Calculate the initial value (R0)
    current_value = 0
    sum_of_elements = 0
    
    for i in range(n):
        current_value += i * a[i]
        sum_of_elements += a[i]
    
    max_value = current_value
    
    # Step 2: Calculate all other configurations by rotating the array
    for i in range(1, n):
        current_value = current_value + sum_of_elements - n * a[n - i]
        if current_value > max_value:
            max_value = current_value
    
    return max_value
