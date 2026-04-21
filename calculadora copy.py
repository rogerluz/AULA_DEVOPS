import keyboard


op = ""
numb1 = ""
numb2 = ""
final = 0
evento = ""


#

# mais um comentário testando o teste


def handle_key(event):
    global evento
    evento = event.name
    return evento


while True:
    keyboard.on_press(handle_key)
    tecla = evento
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
        n1 = int(numb1)
        n2 = int(numb2)
        match op:
            case 's':
                final = n1 + n2
                tecla = ""
                op = ""
                break
            case 'd':
                final = n1 - n2
                tecla = ""
                op = ""
                break
tecla = "o"
op = ""
print(final)
