#Automated Report to see Which users are currently connected to which machines.

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and machines[event.machine] == event.user:
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{} {}".format(machine, user_list))



class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user




events = [
    Event('2020-01-21 12:45:27', 'login', 'workstation.local', 'Joshua'),
    Event('2020-01-22 12:12:55', 'logout', 'workstation.one', 'Martha'),
    Event('2020-01-22 12:16:56', 'logout', 'MainServer', 'Josh'),
    Event('2020-01-21 12:23:52', 'login', 'ftpserver.local', 'Ken'),
    Event('2020-01-21 12:10:33', 'login', 'ftpserver.local', 'Sid')
] 


users = current_users(events)
print(users)

