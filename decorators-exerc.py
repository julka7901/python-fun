# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
def authenticated(fn):
    def wraper(*args, **kwargs):
        if args[0]['valid']: #sprawdzenie 
            return fn(*args, **kwargs)
        else:
            print("nie")
    return wraper
        
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
print(user1['valid'])