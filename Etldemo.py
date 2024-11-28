import json

def transform_data_a(data):
    # Transformation logic for Client A
    data['new_field_a'] = data['field1'] + data['field2']
    return data

def transform_data_b(data):
    # Transformation logic for Client B
    data['new_field_b'] = data['field3'] * 2
    return data

def transform_data_c(data):
    # Transformation logic for Client C
    data['new_field_c'] = data['field4'].upper()
    return data

def etl_process(client_id, json_data):
    # Map client IDs to their respective transformation functions
    client_transform_map = {
        'client_a': transform_data_a,
        'client_b': transform_data_b,
        'client_c': transform_data_c,
    }

    # Get the appropriate transformation function based on the client ID
    transform_func = client_transform_map.get(client_id.lower())

    if transform_func:
        # Apply the transformation
        transformed_data = transform_func(json.loads(json_data))
        return json.dumps(transformed_data)
    else:
        return "Client ID not recognized"

# Example usage:
client_id = "CLIENT_A"
json_data = '{"field1": 10, "field2": 20, "field3": 5, "field4": "hello"}'

transformed_data = etl_process(client_id, json_data)
print(transformed_data)
