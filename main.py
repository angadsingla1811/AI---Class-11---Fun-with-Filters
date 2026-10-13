#Fun with filters
import cv2
import numpy as np

def apply_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == 'red_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == 'green_tint':
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'blue_tint':
        filtered_image[:, :, 2] = 0
        filtered_image[:, :, 1] = 0
    elif filter_type == 'increase_red':
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == 'increase_green':
        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], 50)
    elif filter_type == 'decrease_blue':
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    return filtered_image

image_path = 'image.jpg'
image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not read the image from {image_path}. Please check the file path.")
else:
    filter_type = "original"
    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("g - Green Tint")
    print("b - Blue Tint")
    print("R - Increase Red")
    print("G - Increase Green")
    print("B - Decrease Blue")
    print("q - Quit")

    while True:
        if filter_type == "original":
            filtered_image = image.copy()
        else:
            filtered_image = apply_filter(image, filter_type)
        cv2.imshow('Filtered Image', filtered_image)
        key = cv2.waitKey(0) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('R'):
            filter_type = "increase_red"
        elif key == ord('G'):
            filter_type = "increase_green"
        elif key == ord('B'):
            filter_type = "decrease_blue"
        else:
            print("Invalid key pressed. Please try again.")

    cv2.destroyAllWindows()