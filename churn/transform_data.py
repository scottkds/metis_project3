# Imports
from collections import Counter, defaultdict
import numpy as np

def transform_data(data):
    data = data.split(',')

    # All states in sorted order
    states= ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC',
     'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN',
     'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN',
     'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ',
     'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI',
     'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA',
     'WI', 'WV', 'WY']

    # All necessary keys for a prediction
    all_keys = {'account_length': int, 'international_plan': str,
        'voice_mail_plan': str,
        'number_vmail_messages': int, 'total_day_minutes': float,
        'total_day_calls': int,
        'total_day_charge': float, 'total_eve_minutes': float,
        'total_eve_calls': int,
        'total_eve_charge': float, 'total_night_minutes': float,
        'total_night_calls': int,
        'total_night_charge': float, 'total_intl_minutes': float,
        'total_intl_calls': int,
        'total_intl_charge': float, 'customer_service_calls': int,
        'AK': int, 'AL': int, 'AR': int,
        'AZ': int, 'CA': int, 'CO': int, 'CT': int, 'DC': int, 'DE': int, 'FL': int, 'GA': int,
        'HI': int, 'IA': int, 'ID': int, 'IL': int, 'IN': int, 'KS': int, 'KY': int, 'LA': int,
        'MA': int, 'MD': int, 'ME': int, 'MI': int, 'MN': int, 'MO': int, 'MS': int, 'MT': int,
        'NC': int, 'ND': int, 'NE': int, 'NH': int, 'NJ': int, 'NM': int, 'NV': int, 'NY': int,
        'OH': int, 'OK': int, 'OR': int, 'PA': int, 'RI': int, 'SC': int, 'SD': int, 'TN': int,
        'TX': int, 'UT': int, 'VA': int, 'VT': int, 'WA': int, 'WI': int, 'WV': int, 'WY': int,
        408: int, 415: int, 510: int}

    # all_keys = {'account_length', 'international_plan', 'voice_mail_plan',
    #  'number_vmail_messages', 'total_day_minutes', 'total_day_calls',
    #  'total_day_charge', 'total_eve_minutes', 'total_eve_calls',
    #  'total_eve_charge', 'total_night_minutes', 'total_night_calls',
    #  'total_night_charge', 'total_intl_minutes', 'total_intl_calls',
    #  'total_intl_charge', 'customer_service_calls', 'AK', 'AL', 'AR',
    #  'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
    #  'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA',
    #  'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT',
    #  'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY',
    #  'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN',
    #  'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY',
    #  408, 415, 510}


    # Counters fore state and area code
    state_ctr = Counter([data[2]])
    state_ctr
    area_codes_ctr = Counter([data[4]])
    area_codes_ctr

    # Start building an entry to run in the churn model
    entry = {}
    indices = [3,6,7,8,9,10,11,12,13,14,15,16,17,18,19, 20, 21]
    labels = ['account_length', 'international_plan', 'voice_mail_plan',
           'number_vmail_messages', 'total_day_minutes', 'total_day_calls',
           'total_day_charge', 'total_eve_minutes', 'total_eve_calls',
           'total_eve_charge', 'total_night_minutes', 'total_night_calls',
           'total_night_charge', 'total_intl_minutes', 'total_intl_calls',
           'total_intl_charge', 'customer_service_calls']

    # Add keys from the labels list
    for idx, val in enumerate(indices):
        entry[labels[idx]] = data[val]

    # Add keys from states
    for state in states:
        entry[state] = state_ctr[state]

    # Add keys from area_codes
    area_codes = [408, 415, 510]
    for ac in area_codes:
        entry[ac] = area_codes_ctr[ac]

    # For manual validation
    # for key, val in entry.items():
    #     print(key, val)

    for key, function in all_keys.items():
        entry[key] = function(entry[key])

    conv_yes_no = {'yes': 1, 'no': 0}
    entry['international_plan'] = conv_yes_no[entry['international_plan']]
    entry['voice_mail_plan'] = conv_yes_no[entry['voice_mail_plan']]

    del entry['CA']

    assert len(entry.values()) == 70
    assert sum([key in entry for key in all_keys]) == 70

    return entry

if __name__ == '__main__':
    aws = transform_data("Lindy,Jackson,OH,107,415,371-7191,no,yes,26,161.6,123,27.47,195.5,103,16.62,254.4,103,11.45,13.7,3,3.7,1,False")
    aws
    np.array(list(aws.values())).shape
