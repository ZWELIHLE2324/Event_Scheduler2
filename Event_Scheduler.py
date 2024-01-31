import datetime

class EventScheduler:
    def __init__(self):
        self.events = []

    def add_event(self, title, description, date, time):
        try:
            event_date = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            event = {"title": title, "description": description, "datetime": event_date}
            self.events.append(event)
            print(f"Event '{title}' event is been added.")
        except ValueError:
            print("Wrong d format. Please use the format YYYY-MM-DD HH:MM.")

    def list_events(self):
        if not self.events:
            print("nothing here.")
            return

        sorted_events = sorted(self.events, key=lambda x: x["datetime"])
        for event in sorted_events:
            print(f"\nTitle: {event['title']}\nDescription: {event['description']}\n"
                  f"Date and Time: {event['datetime'].strftime('%Y-%m-%d %H:%M')}")

    def delete_event(self, title):
        for event in self.events:
            if event['title'] == title:
                self.events.remove(event)
                print(f"Event '{title}' deleted successfully.")
                return

        print(f"Event with title '{title}' not found.")

def main():
    scheduler = EventScheduler()

    while True:
        print("\nPlease choose one option:")
        print("1. Add Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. exit")

        choice = input("Choose between (1-4): ")

        if choice == '1':
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            scheduler.add_event(title, description, date, time)

        elif choice == '2':
            scheduler.list_events()

        elif choice == '3':
            title = input("Enter title of the event you want to delete: ")
            scheduler.delete_event(title)

        elif choice == '4':
            print("goodbye")
            break

        else:
            print("wrong choice . Pleaseselect between 1 and 4.")

if __name__ == "__main__":
    main()
