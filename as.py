def find_longest_name(names):
    # Your code here
    longest_name = names[0]
    for name in names[1:]:
        if len(name) >= len(longest_name):
            longest_name = name
    return longest_name