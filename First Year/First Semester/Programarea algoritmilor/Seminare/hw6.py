#you are given a string of bits of form 00...0011.000, find out the position of the first bit of 1
bits = input()
step = 1
while step < len(bits): # the smallest power of 2 that is not less than the length
    step *= 2
curr = 0
while step > 0: # we process bits in decreasing order of their 
    if curr + step < len(bits) and bits[curr + step] == '0': # if we add this bit in the position we are still on a 0
        curr += step # we add to the position
    step //= 2 # next bit
curr += 1 # we were at last 0, we increment and now we are at first 1
print(curr)
