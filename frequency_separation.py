import cv2
import numpy as np
import torch
from PIL import Image

class FrequencySeparation:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "blur_radius": ("INT", {
                    "default": 3,
                    "min": 1,
                    "max": 50,
                    "step": 1,
                    "display": "slider"
                }),
            },
        }

    RETURN_TYPES = ("IMAGE", "IMAGE")
    RETURN_NAMES = ("high_freq", "low_freq")
    FUNCTION = "separate"
    CATEGORY = "image/filters"

    def separate(self, image, blur_radius):
        batch, height, width, channels = image.shape

        # Ensure blur_radius is an odd number
        if blur_radius % 2 == 0:
            blur_radius += 1

        # Convert tensor to NumPy array and process each image in the batch
        image = image.cpu().numpy()  # (batch, height, width, channels)

        high_freq_images = []
        low_freq_images = []

        for i in range(batch):
            img = image[i]
            img = img.astype("float32")

            # Debugging: Print the shape of the image
            print(f"Processing image {i + 1}/{batch} with shape: {img.shape}")

            try:
                # Create low pass filter by blurring the original image
                blur = cv2.GaussianBlur(img, (blur_radius, blur_radius), 0)
                low_freq = blur

                # Create high pass filter from the grayscale image
                gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                blur_gray = cv2.GaussianBlur(gray, (blur_radius, blur_radius), 0)
                high_freq = gray - blur_gray + 0.5

                # Ensure high_freq is in the correct range
                high_freq = np.clip(high_freq, 0, 1)

                # Stack high frequency to RGB channels for consistency
                high_freq_rgb = np.stack([high_freq]*3, axis=-1)

                high_freq_images.append(high_freq_rgb)
                low_freq_images.append(low_freq)
            except cv2.error as e:
                print(f"Error processing image {i + 1}/{batch}: {e}")

        if not high_freq_images or not low_freq_images:
            raise ValueError("No valid images processed. Please check input image dimensions.")

        # Convert lists to tensors
        high_freq_result = torch.from_numpy(np.stack(high_freq_images)).permute(0, 1, 2, 3).float()
        low_freq_result = torch.from_numpy(np.stack(low_freq_images)).permute(0, 1, 2, 3).float()

        return (high_freq_result, low_freq_result)

    @staticmethod
    def tensor_to_image(tensor):
        # Convert tensor to NumPy array
        array = tensor.squeeze().permute(1, 2, 0).cpu().numpy()
        array = (array * 255).clip(0, 255).astype(np.uint8)
        return Image.fromarray(array)

NODE_CLASS_MAPPINGS = {
    "FrequencySeparation": FrequencySeparation
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrequencySeparation": "Frequency Separation Node"
}
