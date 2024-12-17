import matplotlib.pyplot as plt
import pandas as pd

# List of high CV machines
List_of_high_CV = [
    ('4e1ad3a9-c947-4a99-9bbe-6a01c669bc53', 1.4), ('f1aa0c14-7014-4491-acff-82953c519abc', 1.38), 
    ('5e3b87d4-640f-4234-9b20-60620429cbf3', 1.08), ('8ebb2dbe-f83d-42d1-86e2-073392f7a343', 1.06), 
    ('455875d0-b14e-47ed-a8f2-f3bdd9ae23ff', 1.04), ('e66f2425-2499-493f-a5a4-ff3b2d3eff51', 1.02), 
    ('8e18b765-f76a-44ff-956e-5af377d94621', 1.02), ('49594d0d-8d1f-4add-a559-f9b63f740037', 0.95), 
    ('0510b4df-b0be-4dc4-b81e-2b288516fd6b', 0.93), ('67ddd3a1-d630-49b1-83aa-2f87053bd513', 0.89), 
    ('9e3fd9ab-dbe6-4b83-b367-11df51d6512d', 0.85), ('61fbaddf-5461-4f2e-bb49-1abe9c77aba3', 0.85), 
    ('3f8809cd-3de4-4a98-bc4f-752213b8af39', 0.85), ('7f48cf4d-daa3-499b-9866-9caa128805bf', 0.82), 
    ('61d1dfad-5c94-45c5-9618-4f92f69ccc4e', 0.8), ('ab39b18a-9ad9-413b-b436-9678d4be4bc0', 0.79), 
    ('6dbc170f-b1a5-4668-8004-cc7aa9fbdc2a', 0.79), ('5839e957-47b5-4628-8430-03a1ef611a2c', 0.78), 
    ('5416bd19-2830-4c81-bca9-63c3ab7fefce', 0.77), ('d63f2c8b-8be7-4809-b496-b0fa463549bb', 0.75), 
    ('c3f68b78-e1b5-475e-a606-dd00fcb95fa7', 0.74), ('5cfd2ab4-074c-4cf6-91e2-0beb5b5cfcbe', 0.71), 
    ('2ad4c9f5-34b7-4ab4-8e13-6ef548cad5e5', 0.71), ('70c38b57-79fb-4323-b92d-fdeccbdf05cc', 0.65), 
    ('aef7a909-6f1f-4ae5-9d03-f3e17b28344f', 0.64), ('654a3bb7-5669-4d42-b37d-50e153a9d1e4', 0.64), 
    ('166ceebe-f42f-49a1-bf42-73697942238e', 0.6), ('50de6e02-c915-4fc6-aa26-fe2ba6598c57', 0.58), 
    ('de7e208c-cd6c-4946-b384-74064878123c', 0.56), ('69f225de-5d9b-4bff-9214-dbb0881a31ce', 0.56), 
    ('32be0c37-a9b1-4de2-a17a-bba8a87b61d0', 0.54), ('6304483c-ddd0-428f-b43b-20c1a0cef904', 0.53), 
    ('1200c9e3-091c-4634-af71-0503567b2271', 0.51), ('4ee5f1a2-042f-43c0-851d-f45f5fb05dac', 0.49), 
    ('09c7950a-0b23-4d1c-91f3-502c8a14444a', 0.47), ('aaf98747-fa11-4aa0-a4f0-40b23c6b09c3', 0.4)
]

# Load the data from JSON file with error handling
file_path = '/Users/paullemaire/Documents/data2024.json'
try:
    df = pd.read_json(file_path, lines=True)
except ValueError as e:
    print(f"Error reading JSON file: {e}")
    exit(1)

# Convert List_of_high_CV to a set for faster lookups
high_cv_devices = set(device_id for device_id, _ in List_of_high_CV)

# Create a dictionary to store device ID to client ID mapping
device_to_client = dict(zip(df['Downlink-CRM-DeviceID'], df['Downlink-CRM-ClientID']))

# Initialize a dictionary to store client counts
client_counts = {}

# Count the occurrences of each device in List_of_high_CV
for device_id, _ in List_of_high_CV:
    if device_id in device_to_client:
        client_id = device_to_client[device_id]
        if client_id in client_counts:
            client_counts[client_id] += 1
        else:
            client_counts[client_id] = 1

# Print the result
print(client_counts)