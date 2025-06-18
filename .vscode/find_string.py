def count_substring(string,sub_string):
    length=len(sub_string)
    NEW=[]
    for i in range(len(string)-length+1):
        new=[string[i:i+length]]
        NEW.append(new)
    
    WORDS=[]
    count=0
    for word in NEW:
        if sub_string in word:
            WORDS.append(sub_string)
    
    return len(WORDS)
            
        
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)