"""Mini AI Chatbot"""

def main():
    """Main Function"""
    for _ in range(int(input())):
        text = input().lower()
        words = [w.strip("0123456789!.,?") for w in text.split()]
        if "hello" in words or "hi" in words:
            print("Hello! How can I help you?")
        elif "bye" in words or "goodbye" in words:
            print("Goodbye! Have a nice day!")
        elif text.endswith("?"):
            print("That's an interesting question!")
        elif any(t.isnumeric() for t in text):
            print("I see some numbers there!")
        elif len(text) > 20:
            print("That's quite a long message!")
        else:
            print("I understand.")

main()
