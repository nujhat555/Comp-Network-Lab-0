

# Fill these in from your own course materials/account.
SLACK_PASSPHRASE = "pcap"  # exact passphrase posted by a TA in Slack
NYU_EMAIL = "nmc9486@nyu.edu"  # email used for the SHA-256 answer

# Replace each UNANSWERED value with the answer in the requested type:
# strings for Yes/No and the hash; integers for TCP/IP layer numbers.
UNANSWERED = object()


def welcome_assignment_answers(question):
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = SLACK_PASSPHRASE
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = UNANSWERED  # TODO: enter "Yes" or "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = UNANSWERED  # TODO: enter "Yes" or "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = UNANSWERED  # TODO: enter "Yes" or "No"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = UNANSWERED  # TODO: enter "Yes" or "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "212144ad055ff7b15e1a52b217d123a507582c6be65e47c93d795543c66f7fa9"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = UNANSWERED  # TODO: enter "Yes" or "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = UNANSWERED  # TODO: enter an integer
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = UNANSWERED  # TODO: enter an integer
    else:
        # Keeping a fallback prevents an unknown question from leaving answer unset.
        return "This is not my beautiful wife! This is not my beautiful car! How did I get here?"

    if answer is UNANSWERED or answer is None:
        raise ValueError("Complete the TODO for this question before submitting.")
    return answer


if __name__ == "__main__":
    # Replace this with one question you have completed to test your answer.
    debug_question = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
    try:
        print(welcome_assignment_answers(debug_question))
    except ValueError as error:
        print(error)
