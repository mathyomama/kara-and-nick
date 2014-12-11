import os
import sys

PASSWORD = "Tampa2014"
FILE = "usernames.csv"

def populate(option):
    with open(FILE) as filename:
        for line in filename:
            name, name_on_invitation, username, reservations = line.split(',')
            if option == "create":
                try:
                    user = create_user(username, PASSWORD)
                    account = create_account(user, int(reservations))
                except Exception as e:
                    print e
                    print username, reservations
                    print "skipping %s" % line.strip()
            elif option == "delete":
                delete_user_and_account(username)
            else:
                print "I don't understand that command. Give me 'create' or 'delete' , please."

def delete_user_and_account(username):
    try:
        u = User.objects.get(username=username)
        a = Account.objects.get(user=u)
        a.delete()
        u.delete()
    except:
        print "User or Account, %s, doesn't exist." % username

def create_user(username, password):
    u = User.objects.get_or_create(username=username)[0]
    u.set_password(password)
    u.save()
    return u

def create_account(user, reservations):
    a = Account.objects.get_or_create(user=user, reservations=reservations)
    #print "Created account %s" % a
    return a

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedding.settings')
    import django
    django.setup()
    from django.contrib.auth.models import User
    from rsvp.models import Account
    try:
        populate(sys.argv[1])
    except IndexError:
        print "Feed me an argument; I am hungry, RAWR."
