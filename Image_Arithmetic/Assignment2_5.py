import cv2
import numpy as np
import random

def add_salt_pepper_noise(image, p):
    noisy_image = image.copy()
    rows, cols = noisy_image.shape[:2]
    num_pixels_to_change = int(p * rows * cols)

    for _ in range(num_pixels_to_change):
        # Randomly pick a row, col
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        # Randomly decide salt (white) or pepper (black)
        if random.random() < 0.5:
            # pepper
            noisy_image[r, c] = [0, 0, 0]
        else:
            # salt
            noisy_image[r, c] = [255, 255, 255]

    return noisy_image

def bilinear_filter_r_channel(r_channel):
    """
    Apply a 3x3 'bilinear' filter to each pixel in the R channel.
    For demonstration, we'll do a simplified approach:
    - For each pixel (not at boundary), average the 4 corners around it.
    - For boundary pixels, skip or do something simple.
    """
    # We'll create an output channel same size as r_channel
    rows, cols = r_channel.shape
    output = np.zeros_like(r_channel)  # same shape, uint8

    # We'll just skip the boundary for simplicity
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # corners in 3x3 block
            R_tl = r_channel[i-1, j-1]
            R_tr = r_channel[i-1, j+1]
            R_bl = r_channel[i+1, j-1]
            R_br = r_channel[i+1, j+1]
            # bilinear interpolation weight for center is 0.25 for each corner
            val = 0.25*(R_tl + R_tr + R_bl + R_br)
            output[i, j] = np.clip(round(val), 0, 255)
    
    # For boundary pixels, let's just copy them from original or do something naive
    output[0, :] = r_channel[0, :]
    output[-1,:] = r_channel[-1,:]
    output[:, 0] = r_channel[:, 0]
    output[:, -1] = r_channel[:, -1]

    return output

def main():
    # 1. Open a color image
    img_path = 'luffy.jpg'
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Could not read the image file.")
        return

    # Display the original image
    cv2.imshow("Original Image", img)
    print("Displaying original image. Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyWindow("Original Image")


    # For p=0.50
    noisy_img = add_salt_pepper_noise(img, 0.50)
    cv2.imshow("Noisy Image (p=0.50)", noisy_img)
    print("Noisy image displayed for p=0.50. Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyWindow("Noisy Image (p=0.50)")

    row, col = 100, 100  # choose a pixel away from edges

    # 1) Print the pixel's neighborhood
    neighborhood = noisy_img[row-1:row+2, col-1:col+2]
    print("Neighborhood BGR values:")
    for rr in range(3):
        for cc in range(3):
            b, g, r_val = neighborhood[rr, cc]
            print(f"({row-1+rr},{col-1+cc}) -> B={b}, G={g}, R={r_val}")
        print()

    # 2) Manual calculation
    # B channel (box)
    b_vals = [neighborhood[rr, cc, 0] for rr in range(3) for cc in range(3)]
    b_box = sum(b_vals)/9.0

    # G channel (median)
    g_vals = [neighborhood[rr, cc, 1] for rr in range(3) for cc in range(3)]
    g_vals.sort()
    g_median = g_vals[4]

    # R channel (bilinear: average corners)
    R_tl = neighborhood[0,0,2]
    R_tr = neighborhood[0,2,2]
    R_bl = neighborhood[2,0,2]
    R_br = neighborhood[2,2,2]
    r_bilinear = 0.25*(R_tl + R_tr + R_bl + R_br)

    manual_b = int(round(b_box))
    manual_g = int(round(g_median))
    manual_r = int(round(r_bilinear))
    print(f"Manually calculated denoised pixel = (B={manual_b}, G={manual_g}, R={manual_r})")

    # 3) Officially apply the combined approach to entire image
    b_channel, g_channel, r_channel = cv2.split(noisy_img)
    
    B_box = cv2.blur(b_channel, (3,3))
    G_median = cv2.medianBlur(g_channel, 3)
    R_bilinear = bilinear_filter_r_channel(r_channel)

    combined = cv2.merge([B_box, G_median, R_bilinear])
    final_pixel = combined[row, col]
    print(f"Pixel in final denoised image = (B={final_pixel[0]}, G={final_pixel[1]}, R={final_pixel[2]})")

    # 4) Compare
    if (final_pixel[0] == manual_b and
        final_pixel[1] == manual_g and
        final_pixel[2] == manual_r):
        print("The calculated value matches the final image's pixel exactly!")
    else:
        print("They differ slightly. Possible reasons: rounding, boundary effects, etc.")


    # End
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
