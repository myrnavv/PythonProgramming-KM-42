import json
with open('image_info_test-dev2017.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

num_images = len(data['images'])
print(f"Кількість фотографій: {num_images}")

num_categories = len(data['categories'])
print(f"Кількість категорій: {num_categories}")

for image in data['images']:
    if image['file_name'] == '000000000001.jpg':
        print('url: ', image['coco_url'])
        print('height: ', image['height'])
        print('width: ', image['width'])
        print('id: ', image['id'])
        
max_number_image = max(data['images'], key=lambda x: x['file_name'].replace('.jpg', ''))
print('Photo with the highest number: ', max_number_image['file_name'])