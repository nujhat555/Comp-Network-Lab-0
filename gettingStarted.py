# Fill these in from your own course materials/account.

SLACK_PASSPHRASE = "pcap"  # exact passphrase posted by a TA in Slack
NYU_EMAIL = "nmc9486@nyu.edu"  # email used for the SHA-256 answer


def welcome_assignment_answers(question):
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = SLACK_PASSPHRASE

    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"

    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"

    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"

    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"

    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "212144ad055ff7b15e1a52b217d123a507582c6be65e47c93d795543c66f7fa9"

    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"

    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 4

    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 2

    else:
        return "This is not my beautiful wife! This is not my beautiful car! How did I get here?"

    return answer


if __name__ == "__main__":
    debug_question = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
    print(welcome_assignment_answers(debug_question))
