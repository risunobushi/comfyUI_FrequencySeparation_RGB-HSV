import cv2
import numpy as np
import torch

class FrequencyCombinationHSV:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "high_freq": ("IMAGE",),
                "low_freq": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "combine"
    CATEGORY = "image/filters"

    def combine(self, high_freq, low_freq):
        batch, height, width, channels = high_freq.shape

        # Convert tensors to NumPy arrays
        high_freq = high_freq.cpu().numpy()  # (batch, height, width, channels)
        low_freq = low_freq.cpu().numpy()  # (batch, height, width, channels)

        combined_images = []

        for i in range(batch):
            high = high_freq[i]
            low = low_freq[i]

            # Check if low image has 3 channels
            if low.shape[2] != 3:
                raise ValueError(f"Low frequency image at index {i} does not have 3 channels")

            # Convert low frequency image to HSV
            low_hsv = cv2.cvtColor(low, cv2.COLOR_RGB2HSV)
            h, s, v_low = cv2.split(low_hsv)

            # Linear light blending on V channel
            v_combined = (2 * v_low + high[..., 0] - 1).clip(0, 1)

            # Recombine the channels
            combined_hsv = cv2.merge([h, s, v_combined])
            combined_rgb = cv2.cvtColor(combined_hsv, cv2.COLOR_HSV2RGB)

            combined_images.append(combined_rgb)

        # Convert list to tensor
        combined_result = torch.from_numpy(np.stack(combined_images)).permute(0, 1, 2, 3).float()

        return (combined_result,)


NODE_CLASS_MAPPINGS = {
    "FrequencyCombinationHSV": FrequencyCombinationHSV
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrequencyCombinationHSV": "Frequency Combination HSV Node"
}
