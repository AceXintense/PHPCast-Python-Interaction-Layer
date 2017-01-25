import requests
from lib.config import get_domain


def skip_to_next_file(session):
    try:
        print('Skipping to next file in the queue.')
        return session.put(get_domain() + 'skipToNext', timeout=0.1)
    except:
        return ''


def main():
    session = requests.session()
    skip_to_next_file(session)
    session.close()


main()
