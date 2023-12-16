



with open('Input/Letters/starting_letter.txt') as data:
    with open('Input/Names/invited_names.txt') as name_file:
        letter_read_data = data.read()
        lines = name_file.readlines()
        for name in lines:
            new_name = name.strip()
            

            new_to_send = letter_read_data.replace('[name]',str(new_name))
            with open(f'Output/ReadyToSend/{new_name}.txt','w') as write_file:
                write_file.write(new_to_send)

            
           
     
