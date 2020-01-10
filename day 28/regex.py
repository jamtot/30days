"""Use regular expressions to validate inputs."""

import re

if __name__ == '__main__':
    N = int(input())

    NAME_PATTERN = "^[a-z]{1,20}$"
    EMAIL_PATTERN = r"^[a-z](\.?[a-z]){0,50}@gmail\.com$"
    NAME_LIST = list()

    for N_itr in range(N):
        first_name_email_ID = input().split()

        first_name = first_name_email_ID[0]

        email_ID = first_name_email_ID[1]

        name_OK = re.match(NAME_PATTERN, first_name)
        email_OK = re.match(EMAIL_PATTERN, email_ID)

        if name_OK and email_OK:
            NAME_LIST.append(first_name)

    print(*sorted(NAME_LIST), sep='\n')
