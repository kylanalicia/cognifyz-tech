for i in range(9):  
    # Inner loop to control the no. of hashes printed per row
    for j in range(9 - i):  # Decreasing no. of hashes per row
        print("# ", end="")  # Print hash with space

    print()  # Move to the next line after each row