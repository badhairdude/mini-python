

username = str(input("What is your username?\n"))

symbol = "*"
start_symbol = ".::"
end_symbol = "::."
length_user = len(username) + len(start_symbol) + len(end_symbol)

print(symbol * length_user)
print(start_symbol + username + end_symbol)
print(symbol * length_user)
