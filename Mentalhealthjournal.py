import datetime

class MentalHealthEvent:
    def __init__(self, event_type, date, description):
        self.event_type = event_type
        self.date = date
        self.description = description

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - Event Type: {self.event_type}, Description: {self.description}"

class MentalHealthJournal:
    def __init__(self):
        self.entries = []

    def log_entry(self, event_type, description):
        entry = MentalHealthEvent(event_type, datetime.datetime.now(), description)
        self.entries.append(entry)
        print(f"Event logged.")

    def review_entries(self):
        for entry in self.entries:
            print(str(entry))

# Sample usage
if __name__ == "__main__":
    mh_journal = MentalHealthJournal()

    mh_journal.log_entry("Anxiety episode", "Felt like I was talking to someone else, but then realized I was alone.")
    mh_journal.log_entry("Imagination/Reality confusion", "Had a vivid daydream and temporarily couldn't tell if it was real or not.")
    mh_journal.log_entry("Mood swing", "Suddenly felt very sad for no apparent reason.")

    print("\nReviewing entries:")
    mh_journal.review_entries()
