import keyboard
op = ""
numb1 = ""
numb2 = ""
final = 0

while True:
    tecla = keyboard.read_key()
    if tecla != "c":
        if tecla not in ['s', 'd', 'c'] and op == "":
            numb1 += tecla
            continue
        elif tecla in ['s', 'd']:
            op = tecla
        elif tecla not in ['s', 'd', 'c']:
            numb2 += tecla
            continue
    else:
        match op:
            case 's':
                n1 = int(numb1)
                n2 = int(numb2)
                final = n1 + n2
                break
            case 'd':
                n1 = int(numb1)
                n2 = int(numb2)
                final = n1 - n2
                break
print(final)
      
        
        
  



    
