
def convert(message):
    message1 = message.replace(':)','🙂')
    message2 = message.replace(':(','🙁')
    return message2

    def main():
        input_message = input("Enter a message: ")
        converted_message = convert(input_message)
        print(converted_message)

    if __name__ == "__main__":
        main()
        