from sys import argv

script, user_name = argv

prompt = '> '

print(f"Hi {user_name}")
print(f"I'd like to ask you a few")
print("")
likes = input(prompt)

print(f"Where do you live")
lives = input(prompt)

print(f"What kind of computer do you have")
computer = input(prompt)

print(f"""
Alright,
""")