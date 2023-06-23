#!/usr/bin/python3
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
    
    if text.strip() == "help" or "example":
	printr("")
	print("Here is an example to coding Sython...")
	print("type('hello world')")
	print("hello world")
	print("")
 	print("1000 + 922")
	print("1922")
	continue

    if text.strip() == "about" or "ShevamV Code" or "S_Code":
        print()
        print("ShevamV Code Language (SCL)")
        print("Version Py3 0.1, SystoCode 01")
        print()
        print("© Pythowo, Viraj Dasani")
        print("UWU Programming langauge")
        print()
        print("E-mail")
        print("Vermans.svr@gmail.com")
        print()
        print("Website")
        print("https://ShevamV-Website.web.app")
        continue
    
    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
