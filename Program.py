import Call
import Organization
import Person
import datetime
import pickle #why is this module lower case, isn't it a class?


def add_person():
    new_person = Person.Person()
    new_person.first_name = input('First Name: ')
    new_person.last_name = input('Last Name: ')

    #adds a new org every time
    #todo: search for an existing org
    #todo: if org name exists use that one
    new_person.organization = Organization.Organization()
    new_person.organization.name = input('Organization: ') #is there any way to refactor the long dot notation?
    return new_person

def add_call():
    new_call = Call.Call()
    new_call.call_datetime = datetime.datetime.today()
    new_call.subject = input('Subject: ')
    new_call.conversation = input('Conversation: ')
    return new_call

def save_all():
    with open('people_data.pkl', 'wb') as output:
        pickle.dump(new_people, output, pickle.HIGHEST_PROTOCOL)

def load_all():
    try:
        with open('people_data.pkl', 'rb') as input:
            return pickle.load(input) #return people
    except:
        pass

data = load_all()
new_people = None
if data is not None:
    new_people = load_all()
else:
    new_people = []

new_person = add_person()
new_call = add_call()
new_person.call = new_call
new_people.append(new_person)
save_all()

for person in new_people:
    print('Hello {} {} from {}.'.format(person.first_name, person.last_name, person.organization.name))

    if person.call is not None:
        print('You called about {} on {}'.format(person.call.subject, person.call.call_datetime))