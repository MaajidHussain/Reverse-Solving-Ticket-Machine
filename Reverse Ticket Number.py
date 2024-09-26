def TicketMachine(Number):
    if Number=="":
        return "Empty Number is not valid."
    reverseNumber=''
    for i in range(len(Number)-1,-1,-1):
        reverseNumber+=Number[i]
    return str(int(reverseNumber))

print(TicketMachine("320"))
print(TicketMachine("132"))
print(TicketMachine("5"))
print(TicketMachine("0"))
print(TicketMachine(""))
print(TicketMachine("00320"))
print(TicketMachine("1000"))