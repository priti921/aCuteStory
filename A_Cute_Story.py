#A cute story of a cat :)
#The story
story = '''
  (\_/)
  (`_`)
  (> )>o I was going to give you this
  U U cookie


  ...(\_/)
  ...(`_`)
  ..o<( <) But then I was like...
  ....U U

  .(\__/)
  ..(O.O)
  ..(>o<) IT`S MY COOKIE!!!
  .. U U

  (\_/)
  (`_`)
  (> )>o Then I said sharing is caring...
  U U

  ...(\_/)
  ...(`_`)
  .o<( <) But then I was like...
  ...U U
  .(\__/)
  .(O.O)
  .(>o<) I LIKE COOKIES TO MUCH TO SHARE!
  ..U U

  (\_/)
  (^_^)
  (> <) So then I ate it...Sorry.'''
print("Hey there! wanna hear a story?")
print("Yes or no[say yes!]")
#Asks for input
x = input()
if x == "yes" or x == "Yes":
  #The story
  print(story)
  print('''
  
  How do you like that?(̿▀̿‿ ̿▀̿ ̿)''')
elif x == "no" or x == "No":
  print("Oh comon, just say yes :|")
  x = input()
  if x == "yes" or x == "Yes":
    print(story)
  else:
    print('''     ┬─┬ ノ( ゜-゜ノ)

     Am I A Joke To You !?

    ノ ゜Д゜)ノ ︵ ┻━┻ ''')
else:
  print("Do it right, will ya (눈_눈)")

