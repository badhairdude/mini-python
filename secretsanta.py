import random

import smtplib

print("Welcome to Chris's Secret Santa Game\n\n Secret Santa is a game where you secretly matched up to one of your friends.")
print("Once matched, you have to give them a gift that is worth less than $10")
print("To start, please enter in the prompts below")

while True:
    try:
        number_of = int(input("How many people are participating? "))
        break
    except ValueError:
        print("Enter a number, foo!")


people_dict = {}

for num in range(number_of):
    list_of = []
    name_of = "Person " + str(num+1)
    name = str(input("What's your name Person " + str(num+1)+ " ? "))
    email = str(input("What's your email address? "))
    gift = str(input("What do you want? "))
    list_of.append(name)
    list_of.append(email)
    list_of.append(gift)
    people_dict[name_of] = list_of

#people_dict_copy = people_dict
santa_assignment = {}

while len(santa_assignment) < number_of:
    for key in people_dict:
        random_user = random.sample(list(people_dict), 1)
        if key not in santa_assignment and key != random_user[0]:
            print(key + " is assigned to " + (random_user[0]))
            info = people_dict.get(key, "N/A")
            info_assigned = people_dict.get(random_user[0], "N/A")
            print(info[0] + ", you got assigned to " + info_assigned[0] )
            print(info_assigned[0] + "'s email address is " + info_assigned[1] + " and they want " + info_assigned[2] + " for Christmas! Good luck!")
            santa_assignment[key] = random_user[0]
            #print(santa_assignment)


def send_email(text):
    TO = 'badhairdude02@gmail.com'
    SUBJECT = 'TEST MAIL'
    #TEXT = 'Here is a message from python.'

    # Gmail Sign In
    gmail_sender = 'christopherstevenlee@gmail.com'
    gmail_passwd = 'eelsirhc632'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', str(text)])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')

    server.quit()

send_email(santa_assignment)
