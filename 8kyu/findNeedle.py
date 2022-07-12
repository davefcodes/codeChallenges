# Instructions 

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says: 
# "found the needle at position " plus the index it found the needle, so

# Example
# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 

# My solution 

def find_needle(haystack):
    # your code here
    return "found the needle at position {}".format(haystack.index("needle"))

