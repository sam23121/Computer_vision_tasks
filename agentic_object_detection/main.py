import os
import numpy as np
from vision_agent.tools import *
# import vision_agent.tools as T
from typing import *
from pillow_heif import register_heif_opener
register_heif_opener()
import vision_agent as va
from vision_agent.tools import register_tool


def count_food_items_in_image(image_path: str) -> dict:
    """
    Count the number of peas, pearl onions, and mushrooms in an image.

    

    :param image_path: The file path (or URL) of the image.
    :return: A dictionary with the final counts for peas, pearl onions, and mushrooms.
    """

    # Step 1: Load the image
    image = load_image(image_path)

    # Step 2: Detect peas with countgd_object_detection
    detections_peas = countgd_object_detection("pea, pearl onion, mushroom", image)
    pea_count = 0
    for det in detections_peas:
        if det["score"] > 0.3 and det["label"] == "pea":
            pea_count += 1

    # Step 3: Detect pearl onions and mushrooms with owlv2_object_detection
    detections_others = owlv2_object_detection("pearl onion, mushroom", image)
    pearl_onion_count = 0
    mushroom_count = 0
    for det in detections_others:
        if det["score"] > 0.3:
            if det["label"] == "pearl onion":
                pearl_onion_count += 1
            elif det["label"] == "mushroom":
                mushroom_count += 1

    # Combine detections just to visualize them together
    combined_detections = []
    combined_detections.extend(detections_peas)
    combined_detections.extend(detections_others)

    # Step 5: Visualize and save the result
    image_with_boxes = overlay_bounding_boxes(image, combined_detections)
    try:
        save_image(image_with_boxes, "assets/final_detections.jpg")
    except Exception as e:
        pass

    # Step 6: Return the final counts and annotated image
    return {
        "peas": pea_count,
        "pearl_onions": pearl_onion_count,
        "mushrooms": mushroom_count,
        "annotated_image": image_with_boxes
    }

def get_saved_detection_images() -> str:
    """
    Get the path to the saved detection visualization image from count_food_items_in_image.

    Returns:
        str: Path to the saved image file containing the visualized detections
    """
    return "final_detections.jpg"


if __name__ == "__main__":
    # Test the function with an example image
    test_image_path = "C:/Users/smlal/Downloads/kinetic.jpeg"  # Replace with your test image path
    result = count_food_items_in_image(test_image_path)
    print(result)


