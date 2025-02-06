import cv2
import numpy as np

def main():
    # 1. Open a color image and display it
    img_path = 'luffy.jpg'
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Could not open or find the image.")
        return

    # Display the original image in a window
    cv2.imshow('Original Image', img)
    print("Displaying original image. Press any key in the image window to continue.")
    cv2.waitKey(0)
    cv2.destroyWindow('Original Image')

    # 2. Loop until exit
    while True:
        print("\nChoose an operation:")
        print("  R: Rotate")
        print("  S: Resize")
        print("  P: Perspective Transformation")
        print("  E: Exit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'r':
            # 3. Rotation
            angle_str = input("Enter angle in degrees (positive for clockwise, negative for counterclockwise): ")
            try:
                angle = float(angle_str)
            except ValueError:
                print("Invalid angle. Please try again.")
                continue

            rows, cols = img.shape[:2]
            # Get the rotation matrix around the center of the image
            M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1.0)
            # Perform the affine transformation (rotation)
            rotated_img = cv2.warpAffine(img, M, (cols, rows))

            cv2.imshow('Rotated Image', rotated_img)
            print("Rotated image displayed. Press any key in the image window to continue.")
            cv2.waitKey(0)
            cv2.destroyWindow('Rotated Image')

        elif choice == 's':
            # 4. Resizing
            fx_str = input("Enter resize factor for width (fx): ")
            fy_str = input("Enter resize factor for height (fy): ")
            try:
                fx = float(fx_str)
                fy = float(fy_str)
            except ValueError:
                print("Invalid resize factors. Please try again.")
                continue

            # Resize the image
            resized_img = cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
            cv2.imshow('Resized Image', resized_img)
            print("Resized image displayed. Press any key in the image window to continue.")
            cv2.waitKey(0)
            cv2.destroyWindow('Resized Image')

        elif choice == 'p':
            # 5. Perspective Transformation
            H = np.array([
                [0.4, -0.4, 190],
                [0.15, 0.4, 100],
                [0.0, 0.0, 1.0]
            ], dtype=float)

            rows, cols = img.shape[:2]
            # Apply warpPerspective using the same image size
            perspective_img = cv2.warpPerspective(img, H, (cols, rows))

            cv2.imshow('Perspective Transform', perspective_img)
            print("Perspective transformed image displayed. Press any key in the image window to continue.")
            cv2.waitKey(0)
            cv2.destroyWindow('Perspective Transform')

        elif choice == 'e':
            # Exit the program
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
