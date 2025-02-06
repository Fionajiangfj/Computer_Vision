# Image Arithmetic, Histogram Equalization, Drawing Application, Geometric Transformation, Noise & Filtering

**Course**: Conputer Vision  

This repository contains my individual work for **Assignment 2**, which focuses on various image processing tasks using OpenCV, including:

1. Image Arithmetic & Histogram Equalization  
2. Drawing Application  
3. Geometric Transformation  
4. Noise & Filtering  
5. Pixel-Level Calculations & Verification  

Below is an overview of each part and the corresponding functionality, code snippets, and sample results.

---

## Table of Contents

- [Part I: Image Arithmetic & Histogram Equalization](#part-i-image-arithmetic--histogram-equalization)
  - [Brightness & Contrast](#brightness--contrast)
  - [Linear Blend](#linear-blend)
  - [Histogram Equalization](#histogram-equalization)
- [Part II: Drawing Application](#part-ii-drawing-application)
- [Part III: Geometric Transformation](#part-iii-geometric-transformation)
- [Part IV: Noise and Filtering](#part-iv-noise-and-filtering)
- [Part V: Calculations](#part-v-calculations)
- [References](#references)
- [How to Run](#how-to-run)

---

## Part I: Image Arithmetic & Histogram Equalization

### Brightness & Contrast
**File**: `Assignment2_1.py` (section handling Brightness/Contrast)

1. **Open a color image and display**  
   - I read the image using `cv2.imread()` and show it with `cv2.imshow()`.

2. **Change Brightness by a constant (e.g., +100)**
   ```python
   # Adding constant brightness
   bright_image = cv2.add(original_image, (100, 100, 100, 0))
