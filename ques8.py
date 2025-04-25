def decode_message(s):
    def helper(s, index, current, result):
        if index == len(s):
            result.append(current)
            return
        
        if s[index] != '0':
            helper(s, index + 1, current + chr(int(s[index]) + 96), result)
        
        if index + 1 < len(s) and '10' <= s[index:index+2] <= '26':
            helper(s, index + 2, current + chr(int(s[index:index+2]) + 96), result)
    
    result = []
    helper(s, 0, "", result)
    return result

encoded_message =input("Enter code: ")
decoded_messages = decode_message(encoded_message)

for message in decoded_messages:
    print(message.upper())
