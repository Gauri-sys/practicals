# Rule-Based Chatbot using Pattern Matching
patterns = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "hey": "Hey! How are you?",
    "how are you": "I am fine. Thank you for asking!",
    "what is your name": "I am a simple rule-based chatbot.",
    "who are you": "I am a chatbot created using Python.",
    "help": "I can respond to simple greetings and questions.",
    "thank you": "You're welcome!",
    "thanks": "You're welcome!",
    "bye": "Goodbye! Have a nice day."
}

exit_commands = ["bye", "exit", "quit"]

print("===================================")
print("      Simple Rule-Based Chatbot")
print("===================================")
print("Chatbot: Hello! I am a simple chatbot.")
print("Chatbot: Type 'bye', 'exit' or 'quit' to end the conversation.\n")

while True:
    user_input = input("You: ")
    user_input = user_input.lower().strip()

    if user_input in exit_commands:
        print("Chatbot: Goodbye! Have a nice day.")
        break

    matched = False
    for pattern, response in patterns.items():
        if pattern in user_input:
            print("Chatbot:", response)
            matched = True
            break

    if matched == False:
        print("Chatbot: Sorry, I don't understand that.")


# 1. Aim
# To design and implement a simple rule-based chatbot using Python that interacts with users by identifying predefined keywords and patterns and providing appropriate responses.
# 2. Theory
# A Rule-Based Chatbot is a simple chatbot that works on predefined rules and patterns to communicate with users. It uses pattern matching to identify keywords or phrases from the user's input and generates a suitable response.

# The chatbot follows an IF-THEN approach, where a particular input pattern is matched with a predefined response.

# In this program:
# - A dictionary is used to store predefined patterns and their responses.
# - The input() function accepts messages from the user.
# - The lower() function converts the input into lowercase.
# - The strip() function removes unnecessary spaces.
# - Pattern matching is performed using a for loop and the in operator.
# - If a matching pattern is found, the chatbot displays the corresponding response.
# - If no pattern matches, the chatbot displays a default message.
# - The chatbot terminates when the user enters bye, exit, or quit.
# 3. Algorithm
# 1. Start the program.
# 2. Create a dictionary containing predefined patterns and their responses.
# 3. Define exit commands such as bye, exit, and quit.
# 4. Display the chatbot welcome message.
# 5. Accept input from the user.
# 6. Convert the input into lowercase and remove extra spaces.
# 7. Check whether the input matches any exit command.
# 8. If an exit command is entered, display a goodbye message and terminate the program.
# 9. Otherwise, compare the user input with the predefined patterns.
# 10. If a pattern matches, display its corresponding response.
# 11. If no pattern matches, display a default message.
# 12. Repeat the process until the user exits.
# 13. Stop.
# 4. Conclusion / Result
# Thus, a simple rule-based chatbot was successfully implemented using Python. It uses predefined patterns and pattern matching to identify user inputs and generate appropriate responses.
# 5. Important Functions Used
# Function / Operator	Purpose
# input()	Accepts user input.
# lower()	Converts text into lowercase.
# strip()	Removes extra spaces.
# while True	Repeats the conversation.
# for loop	Checks predefined patterns.
# in operator	Checks whether a pattern exists in the input.
# break	Terminates the loop.
# print()	Displays output.