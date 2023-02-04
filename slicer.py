def email():
    user_email = input('whats your Email: ')

    
    def word_replacement():
        word_list = user_email
        word_to_replace = input('what word do you want to remove: ')
        what_to_append = input('what word to you want to replace with: ')
        str2 = word_list.replace(word_to_replace, what_to_append)
        print('the original email: ', user_email)
        print('........Email after replacing............')
        print('email with replaced char: ', str2)
    
        # separate username and the domain
        (userame, doamin) = str2.split('@')
        # separete the domain and the extensiion
        (doamin, extension) = doamin.split('.')    
        print('Username: ', userame)
        print('Domain: ', doamin)
        print('Extension: ', extension)
    word_replacement()    
while True:
    email()