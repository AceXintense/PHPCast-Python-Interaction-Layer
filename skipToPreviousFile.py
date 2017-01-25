import requests
from lib.config import get_domain


def skip_to_previous_file(session):
    try:
        print('Skipping to previous file in the queue.')
        return session.put(get_domain() + 'skipToPrevious', timeout=0.1)
    except:
        return ''


def main():
    session = requests.session()
    skip_to_previous_file(session)
    session.close()


main()
