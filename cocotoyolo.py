import os
import shutil
import random
import json
from PIL import Image

def create_dataset(source_images, source_annotations, dest_folder, total_images=500):
    # Load annotations
    with open(source_annotations, 'r') as file:
        annotations = json.load(file)
    
    # Prepare directory for the dataset split
    for split in ['train', 'val', 'test']:
        os.makedirs(os.path.join(dest_folder, split, 'images'), exist_ok=True)
        os.makedirs(os.path.join(dest_folder, split, 'labels'), exist_ok=True)

    # Collect all image IDs and shuffle
    image_ids = list({ann['image_id'] for ann in annotations['annotations']})
    random.shuffle(image_ids)
    selected_ids = image_ids[:total_images]

    # Calculate split indices
    train_end = int(0.7 * total_images)
    val_end = train_end + int(0.2 * total_images)

    # Define splits
    train_ids = selected_ids[:train_end]
    val_ids = selected_ids[train_end:val_end]
    test_ids = selected_ids[val_end:]

    # Function to copy files and create YOLO annotations
    def process_files(image_ids, split):
        for image_id in image_ids:
            # Image and annotation path
            image_path = os.path.join(source_images, f"{image_id}.jpg")
            label_path = os.path.join(dest_folder, split, 'labels', f"{image_id}.txt")

            # Copy image
            shutil.copy2(image_path, os.path.join(dest_folder, split, 'images', f"{image_id}.jpg"))

            # Open image to get dimensions
            with Image.open(image_path) as img:
                width, height = img.size

            # Filter annotations for the current image
            img_annotations = [ann for ann in annotations['annotations'] if ann['image_id'] == image_id]
            with open(label_path, 'w') as f:
                for ann in img_annotations:
                    category_id = ann['category_id']
                    segmentation = ann['segmentation'][0]  # Assuming the first segmentation
                    # Normalize points
                    points_normalized = []
                    for i in range(0, len(segmentation), 2):
                        norm_x = segmentation[i] / width
                        norm_y = segmentation[i + 1] / height
                        points_normalized.extend([f"{norm_x:.6f} {norm_y:.6f}"])
                    # Write to YOLO format file
                    f.write(f"{category_id} " + ' '.join(points_normalized) + '\n')

    # Process each split
    process_files(train_ids, 'train')
    process_files(val_ids, 'val')
    process_files(test_ids, 'test')



# Example usage
source_images = '/home/akshay/hustle/Yolv9/deep_fashion/images/train'
source_labels = '/home/akshay/hustle/Yolv9/deep_fashion/annotations/instances_train2024.json'
dest_folder = '/home/akshay/hustle/Yolv9/deep_fashion/fashion'

create_dataset(source_images, source_labels, dest_folder)
