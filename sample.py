import json
from helpers.jsonhelpers import CaseInsensitiveDict

if __name__ == "__main__":
    json_data = '''
    {
        "Name": "John Doe",
        "Age": 30,
        "Email": "john.doe@example.com",
        "Address": {
            "Street": "101 Main Street",
            "City": "Hollywood",
            "State": "CA"
        }
    }
    '''

    parsed_data = json.loads(json_data, object_pairs_hook=CaseInsensitiveDict)

    print(json_data)
    print(parsed_data)

    print(f'{parsed_data['name']}')  
    print(f'{parsed_data['age']}')   
    print(f'{parsed_data['email']}') 
    print(f'{parsed_data['address']['street']}')
