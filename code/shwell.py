import os
import pythowo

while True:
    text = input("ShevamV-Code/Terminal--> ")
    
    if text.strip() == "clear":
        os.system('clear' if os.name == 'posix' else 'cls')
        continue
        
    if text.strip() == "":
        continue
    result, error = pythowo.run("<stdin>", text)
    
    if text.strip() == "help":
    	print("")
    	print("Here is an example to coding Sython...")
    	print("type('hello world')")
    	print("hello world")
    	print("")
    	print("1000 + 922")
    	print("1922")
    	continue
    	
    if text.strip() == "about":
        print()
        print("ShevamV-Code-Language(SCL)")
        print()
        print("©Pythowo, Viraj Dasani")
        print("UWU Langauge")
        print()
        print("E-mail")
        print("Vermans.svr@gmail.com")
        print("")
        print("website")
        print("https://shevamv-website.web.aop")
        continue
        
    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))