program = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


print('Welcome to Grad School')
program = text_prompt('What program would you like to join?')

print('You have chosen: ',program)

print('It is your first day of grad school')
print('Suddenly, Satan appears')
program = text_prompt('He says: grad school is hell, would you like to continue?')

print('You lose')
