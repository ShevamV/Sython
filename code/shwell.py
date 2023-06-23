import os
import pythowo

while True:
    text = imput("ShevamV-Code/Terminal-->")

if text.strip() == "clear":
    os.system('clear' if os.name == 'posix' else 'cls')
    continue

if text.strip() == "":
    continue
result, error = pythowo.run("<STDIN>", text)

if text.strip() == "help":
    print("")
    print("This is example for Sython...")
    print("type('hello world')")
    print("hello world")
    print("")
    print("1000 + 200 + 3 * 10 + 10 / 2 - 1")
    print("1234.0")
    continue

if text.strip() == "about":
    print("")
    print("ShevamV Coding Language(SCL)")
    print("")
    print("© Pythowo, Viraj Dasani")
    print("UWU ")