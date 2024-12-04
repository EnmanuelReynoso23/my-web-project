import random

# Import Required Libraries

# Define Data Structures
events = [
    "a great war",
    "a technological breakthrough",
    "a political revolution",
    "a natural disaster",
    "a cultural renaissance"
]

characters = [
    "a brave knight",
    "a cunning politician",
    "a brilliant scientist",
    "a wise philosopher",
    "a fearless explorer"
]

locations = [
    "in the ancient city of Atlantis",
    "in the bustling streets of New York",
    "in the serene mountains of Tibet",
    "in the dense jungles of the Amazon",
    "in the futuristic city of Neo Tokyo"
]

# Generate Random Events
def generate_random_event():
    event = random.choice(events)
    character = random.choice(characters)
    location = random.choice(locations)
    return f"{character} experienced {event} {location}."

# Create Random History
def create_random_history(num_events):
    history = []
    for _ in range(num_events):
        history.append(generate_random_event())
    return history

# Display Generated History
def display_history(history):
    for event in history:
        print(event)

# Example Usage
if __name__ == "__main__":
    num_events = 5
    random_history = create_random_history(num_events)
    display_history(random_history)