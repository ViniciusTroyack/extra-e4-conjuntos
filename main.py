from fruits import spanish_fruits, brazilian_fruits, japanese_fruits, popular_fruits
from email_list import emails

# Fruits
def spanish_and_brazilian_fruits(spanish_fruits, brazilian_fruits):
    return list(spanish_fruits & brazilian_fruits)


def spanish_and_japan_fruits(spanish_fruits, japanese_fruits):
    return list(spanish_fruits & japanese_fruits)


def brazilian_and_japan_fruits(brazilian_fruits, japanese_fruits):
    return list(brazilian_fruits & japanese_fruits)


def popular_spanish_or_brazilian_fruits(popular_fruits, spanish_fruits, brazilian_fruits):
    return list(spanish_fruits | brazilian_fruits & popular_fruits)


def popular_only_spanish_fruits(popular_fruits, spanish_fruits, japanese_fruits, brazilian_fruits):
    return list(japanese_fruits | brazilian_fruits - spanish_fruits & popular_fruits)


# Email
def only_yahoo_emails(emails_list):
    return set([yahoo_email for yahoo_email in emails_list if 'yahoo' in yahoo_email])


def only_hotmail_emails(emails_list):
    return set([hotmail_email for hotmail_email in emails_list if 'hotmail' in hotmail_email])


def only_br_emails(emails_list):
    return set([br_email for br_email in emails_list if br_email.endswith('br')])

