
with open(f'./Output/ReadyToSend/example.txt', 'r') as file:
    letter_content = file.read()

with open('./input/Names/invited_names.txt', 'r') as people:
    x = people.readlines()
    for person in x :
        a = person.strip()
        with open(f'./Output/ReadyToSend/letter_to_{a}.txt', 'w') as file:
            personalized_content = letter_content.replace('name', a)
            file.write(personalized_content)
            print(personalized_content) 
    
    
