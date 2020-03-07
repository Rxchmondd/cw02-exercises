angry = True
bored = True
hungry = False
tired = False

if angry and bored and hungry: 
    print('he will eat the Triceratops')
elif  hungry and tired:
    print('he will eat the Iguanadon')
elif hungry and bored:
    print('he will eat the Stegasaurus')
elif tired:
    print('he goes to sleep')
elif angry and bored:
    print('he will fight with the Velociraptor')
elif angry or bored:
    print('he roars')
else:
    print('Gives a toothy Smile')
