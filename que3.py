def check_quotes(filename):
    with open ('text_file.txt','r') as input_file:
        content=input_file.read()
        
        quotes=0
        for char in content:
            if char=="'" or char=='"':
                quotes+=1
            
        if quotes%2==0:
            return True
        else:
            return False
              
result=check_quotes('text_file.txt')
print(result);