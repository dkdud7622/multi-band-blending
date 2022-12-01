# multi-band-blending
Multi-band blending using the Gaussian and Laplacian pyramids.
If you change the shape of the mask, various synthesis is possible.

# multiBlending
```
 multiBlending(img1,img2,Mask,deep)
```
## img1 & img2
8bit, 3-Channel Color image

## Mask
8bit, 3-Channel Binary image

## deep
Pyramid depth

## Result
### img1
![apple](https://user-images.githubusercontent.com/80615126/204947560-fa0f9ae8-270b-4619-a896-5efa635dd312.png)
### img2
![orange](https://user-images.githubusercontent.com/80615126/204947566-d18af1a7-4115-494b-acf4-7b4f0cbfe71c.png)
### Mask
![mask](https://user-images.githubusercontent.com/80615126/204947571-4a0075c6-2864-4a18-83a8-1a2e1c2dfb1b.png)
### result
![result](https://user-images.githubusercontent.com/80615126/204947525-9893ae0e-484b-405f-8d49-1be98d050d71.png)

# getMask
```
getMask(img)
```
if your Mask Image Not binary, you can use this function to make binary Mask.

## Example
### Input
![testMask](https://user-images.githubusercontent.com/80615126/204948162-fd4f9317-4861-4339-948b-5483f1bc5969.png)
### Output
![binaryMask](https://user-images.githubusercontent.com/80615126/204948424-9a8539d9-ef24-42fc-8fb0-1920d07b7413.png)


# Reference
https://docs.opencv.org/4.x/dc/dff/tutorial_py_pyramids.html
