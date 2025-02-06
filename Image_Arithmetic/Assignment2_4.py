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

    # 2. Ask the user for a probability p
    while True:
        p_str = input("Enter a probability for Salt & Pepper noise (0 <= p <= 1): ").strip()
        try:
            p_val = float(p_str)
            if 0 <= p_val <= 1:
                break
            else:
                print("Probability must be between 0 and 1.")
        except ValueError:
            print("Invalid input. Please enter a numeric value between 0 and 1.")
    
    # 3. Generate the noisy image
    noisy_img = add_salt_pepper_noise(img, p_val)
    cv2.imshow(f"Noisy Image (p={p_val})", noisy_img)
    print(f"Noisy image displayed for p = {p_val}. Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyWindow(f"Noisy Image (p={p_val})")

    # For p=0.10
    noisy_img_10 = add_salt_pepper_noise(img, 0.10)
    cv2.imshow("Noisy Image (p=0.10)", noisy_img_10)
    print("Noisy image displayed for p=0.10. Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyWindow("Noisy Image (p=0.10)")

    # For p=0.20
    noisy_img_20 = add_salt_pepper_noise(img, 0.20)
    cv2.imshow("Noisy Image (p=0.20)", noisy_img_20)
    print("Noisy image displayed for p=0.20. Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyWindow("Noisy Image (p=0.20)")

    # 4. Apply a 3×3 Box Filter on noisy_img (p_val)
    box_3x3 = cv2.blur(noisy_img, (3, 3))
    cv2.imshow("3x3 Box Filter", box_3x3)
    print("3x3 Box-filtered image displayed. Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyWindow("3x3 Box Filter")

    # 5. Apply a 3×3 Median Filter on the same noisy_img
    median_3x3 = cv2.medianBlur(noisy_img, 3)
    cv2.imshow("3x3 Median Filter", median_3x3)
    print("3x3 Median-filtered image displayed. Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyWindow("3x3 Median Filter")

    # 6. Apply a 3×3 Bilateral Filter
    bilateral_3x3 = cv2.bilateralFilter(noisy_img, d=3, sigmaColor=75, sigmaSpace=75)
    cv2.imshow("3x3 Bilateral Filter", bilateral_3x3)
    print("3x3 Bilateral-filtered image displayed. Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyWindow("3x3 Bilateral Filter")

    # 7. Try different kernel sizes of 11x11 and 25x25 for the median, bilateral filter
    median_11x11 = cv2.medianBlur(noisy_img, 11)
    cv2.imshow("11x11 Median Filter", median_11x11)
    print("11x11 Median-filtered image displayed. Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyWindow("11x11 Median Filter")

    box_25x25 = cv2.blur(noisy_img, (25, 25))
    cv2.imshow("25x25 Box Filter", box_25x25)
    print("25x25 Box-filtered image displayed. Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyWindow("25x25 Box Filter")

    # End
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
