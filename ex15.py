from sys import argv

script, filename = argv

txt = open(filename)  # noqa: SIM115

print(f"here is your file: {filename}")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)  # noqa: SIM115

print(txt_again.read())



