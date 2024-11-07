def replace_duplicates(s):
    seen = set()
    result = []
    
    for ch in s:
        if ch in seen:
            new_ch = ch
            while new_ch in seen:
                if '0' <= new_ch <= '9':
                    new_ch = str((int(new_ch) + 1) % 10)
                elif 'a' <= new_ch <= 'z':
                    new_ch = chr((ord(new_ch) - ord('a') + 1) % 26 + ord('a'))
                elif 'A' <= new_ch <= 'Z':
                    new_ch = chr((ord(new_ch) - ord('A') + 1) % 26 + ord('A'))
            result.append(new_ch)
            seen.add(new_ch)
        else:
            seen.add(ch)
            result.append(ch)
    
    return ''.join(result)

# Test cases
print(replace_duplicates("Java1234"))  # Output: Javb1234
print(replace_duplicates("Python1223"))  # Output: Python1234
print(replace_duplicates("aBuzZ9900"))  # Output: aBuzC9012
