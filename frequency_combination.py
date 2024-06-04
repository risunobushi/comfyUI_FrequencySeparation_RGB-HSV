import cv2
import numpy as np
import torch

class FrequencyCombination:
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
        batch, _, height, width = high_freq.shape

        # Convert tensors to NumPy arrays
        high_freq = high_freq.permute(0, 2, 3, 1).cpu().numpy()  # (batch, height, width, channels)
        low_freq = low_freq.permute(0, 2, 3, 1).cpu().numpy()  # (batch, height, width, channels)

        combined_images = []

        for i in range(batch):
            high = high_freq[i]
            low = low_freq[i]

            # Recombine using linear light blending
            v_combined = (2 * high + low - 1).clip(0, 1)

            combined_images.append(v_combined)

        # Convert list to tensor
        combined_result = torch.from_numpy(np.stack(combined_images)).permute(0, 3, 1, 2).float()

        return (combined_result,)


NODE_CLASS_MAPPINGS = {
    "FrequencyCombination": FrequencyCombination
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrequencyCombination": "Frequency Combination Node"
}
