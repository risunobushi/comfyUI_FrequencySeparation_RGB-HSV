# comfyUI_FrequencySeparation_RGB-HSV
A collection of simple nodes for Frequency Separation / Frequency Recombine with RGB and HSV methods

WHAT IS IT

A probably badly coded set of custom nodes for comfyUI dealing with Frequency Separation and Frequency Recombining

WHAT DOES IT DO

Frequency Separation Node - and its sister, Frequency Separation HSV node - splits an image into a High Frequency layer and a Low Frequency layer, either via the standard RGB Gaussian Blur / subtract method, or by the Apply Image to HSV V channel only method.
Frequency Recombine Node - and its sister, Frequency Recombine HSV node - recombines the two High Frequency layer and Low Frequency Layer.

WHY IS IT USEFUL

Since IC-Light came out, I was looking for a way to manipulate the two HF / LF layers independently, to:
- match colors on the LF layers;
- create custom blended HF layers by blending the original image's and the relit image's HF layers;
- more like these.

I explain why I needed it in this series of videos: https://youtu.be/_1YfjczBuxQ

You might find this useful for other stuff, I guess.

IMPORTANT

Since I'm not a coder, by any sort of definition of the word, I probably won't be able to offer support or implement a lot more in this repo.
This is more like a "I needed this, so I built this" thing than a well-maintained node.

HOW TO INSTALL

Just 

git clone 

the repo in your comfyUI custom_nodes folder.

ANYTHING ELSE

Nope. Cheers.
