def rearrange_even_odd(seq):
    if not seq:
        return []
    
    first, *rest = seq
    if first % 2 == 0:
        return [first] + rearrange_even_odd(rest)
    else:
        return rearrange_even_odd(rest) + [first]

# Example usage:
sequence = [1, 2, 3, 4, 5, 6, 7, 8]
result = rearrange_even_odd(sequence)
print(result)
