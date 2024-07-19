import re  # to use escape and sub function

# Create a text file named 'story.txt' in the same directory as this script.
# Make sure to include placeholders in the format <placeholder> within your story (e.g., "Once upon a time, there was a <noun> who loved to <verb>.").

# Read story from file
with open("story.txt", "r") as f:
    story = f.read()


# Extract placeholders
words = set()
target_start = "<"
target_end = ">"
stack = []

for i, char in enumerate(story):
    if char == target_start:
        stack.append(i)
    elif char == target_end and stack:
        start_of_word = stack.pop()
        word = story[start_of_word: i + 1]
        words.add(word)

# Collect user inputs
answers = {}
for word in words:
    while True:
        answer = input(f"Enter a word for {word}: ")
        if answer.strip():  # Ensure input is not empty by removing spaces
            answers[word.lower()] = answer
            break
        else:
            print("Input cannot be empty. Please enter a valid word.")


# Replace placeholders with user inputs
for word in words:
    escaped_word = re.escape(word)  # escape() is used to treat special characters as normal
    story = re.sub(escaped_word, answers[word.lower()], story)  # Find and replace specific word in the string

print(story) #prints new story with users words

#Save the story optional
save_option = input("\nDo you want to save the final story to a new text file? (y/n): ").strip().lower()
if save_option == "y":
    output_filename = input("Enter the filename to save the story (e.g., 'new_story.txt'): ").strip()
    with open(output_filename, "w") as f:
        f.write(story)
    print(f"Story saved to {output_filename}")
else:
    print("Story not saved.")