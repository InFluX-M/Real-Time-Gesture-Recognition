import os

# Dataset paths
input_txt = "./Subject6.txt"  # Replace with your dataset file path
output_dir = "./dataset"
os.makedirs(output_dir, exist_ok=True)

# Function to normalize bounding box coordinates
def normalize_bbox(bbox, img_width, img_height):
    x, y, w, h = bbox
    x_center = (x + w / 2) / img_width
    y_center = (y + h / 2) / img_height
    width = w / img_width
    height = h / img_height
    return x_center, y_center, width, height

# Parse the TXT and convert annotations
with open(input_txt, "r") as f:
    lines = f.readlines()

# Assuming the first line is the header, adjust this if needed
for line in lines[1:]:  # Skip header
    parts = line.strip().split(",")
    rgb_path = parts[0].strip()  # Path to RGB image
    depth_path = parts[1].strip()  # Path to Depth image
    bboxes = parts[2:]  # Extract bounding boxes
    
    # Load image dimensions (replace with actual code to get image dimensions)
    img_width, img_height = 640, 480  # Example dimensions
    
    annotations = []
    for idx, bbox_str in enumerate(bboxes):
        if bbox_str.strip() != "[0 0 0 0]":  # Skip empty bounding boxes
            bbox = list(map(float, bbox_str.strip("[]").split()))
            x_center, y_center, width, height = normalize_bbox(bbox, img_width, img_height)
            annotations.append(f"{idx} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")
    
    # Write annotations to a .txt file
    image_name = os.path.basename(rgb_path).replace("_color.png", "")
    txt_path = os.path.join(output_dir, f"{image_name}.txt")
    with open(txt_path, "w") as txt_file:
        txt_file.write("\n".join(annotations))