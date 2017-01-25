import requests
from lib.config import get_domain


def api_issues():
    print('Cannot communicate with the API.')


def skip_to_next_file(session):
    try:
        print('Skipping to next file in the queue.')
        return session.put(get_domain() + 'skipToNext')
    except:
        api_issues()


def main():
    session = requests.session()
    skip_to_next_file(session)
    session.close()


main()
