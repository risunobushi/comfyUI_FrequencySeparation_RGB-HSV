from .frequency_separation import FrequencySeparation
from .frequency_combination import FrequencyCombination
from .frequency_separation_hsv import FrequencySeparationHSV
from .frequency_combination_hsv import FrequencyCombinationHSV

NODE_CLASS_MAPPINGS = {
    "FrequencySeparation": FrequencySeparation,
    "FrequencyCombination": FrequencyCombination,
    "FrequencySeparationHSV": FrequencySeparationHSV,
    "FrequencyCombinationHSV": FrequencyCombinationHSV,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrequencySeparation": "Frequency Separation Node",
    "FrequencyCombination": "Frequency Combination Node",
    "FrequencySeparationHSV": "Frequency Separation HSV Node",
    "FrequencyCombinationHSV": "Frequency Combination HSV Node"
}
