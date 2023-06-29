import os
import pythowo

while True:
    text = input("ShevamV-Code/Terminal-->")  # Fixed typo: changed "imput" to "input"

    if text.strip() == "clear":
        os.system('clear' if os.name == 'posix' else 'cls')
        continue
    elif text.strip() == "":
        continue

    result, error = pythowo.run("<STDIN>", text)

    if text.strip() == "help":  # Added a colon (:) at the end of the line
        print("")
        print("This is an example for Sython...")
        print("type('hello world')")
        print("hello world")
        print("")
        print("1000 + 200 + 3 * 10 + 10 / 2 - 1")
        print("1234.0")
        continue

    elif text.strip() == "about":
        print("")
        print("ShevamV Coding Language(SCL)")
        print("")
        print("© Pythowo, Viraj Dasani")
        print("UWU programming language")
        print("")
        print("E-mail")
        print("vermans.svr@gmail.com")
        print("Website")
        print("https://shevamv-website.web.app")
        continue

    elif error:
        print(error.as_string())

    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
