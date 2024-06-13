import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

# Function to apply filter to the image
def apply_filter(image, filter_name):
    if filter_name == "Original":
        return image
    elif filter_name == "Grayscale":
        return image.convert("L")
    elif filter_name == "Sepia":
        sepia_filter = np.array([0.272, 0.534, 0.131, 0, 
                                 0.349, 0.686, 0.168, 0, 
                                 0.393, 0.769, 0.189, 0]).reshape((3, 4))
        return Image.fromarray(np.dot(np.array(image), sepia_filter.T).clip(0, 255).astype("uint8"))
    elif filter_name == "Blur":
        return image.filter(ImageFilter.BLUR)
    elif filter_name == "Contour":
        return image.filter(ImageFilter.CONTOUR)
    elif filter_name == "Detail":
        return image.filter(ImageFilter.DETAIL)
    elif filter_name == "Sharpen":
        return image.filter(ImageFilter.SHARPEN)
    elif filter_name == "Contrast":
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(2)
    elif filter_name == "Brightness":
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(1.5)
    return image

# Streamlit app
def main():
    st.title("Image Filter Application")
    
    # Upload image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Select filter
        filter_name = st.selectbox(
            "Select a filter",
            ["Original", "Grayscale", "Sepia", "Blur", "Contour", "Detail", "Sharpen", "Contrast", "Brightness"]
        )
        
        # Apply filter
        filtered_image = apply_filter(image, filter_name)
        
        st.image(filtered_image, caption=f"{filter_name} Image", use_column_width=True)
        
        # Download filtered image
        if st.button("Download Filtered Image"):
            filtered_image.save("filtered_image.png")
            with open("filtered_image.png", "rb") as file:
                btn = st.download_button(
                    label="Download Image",
                    data=file,
                    file_name="filtered_image.png",
                    mime="image/png"
                )

if __name__ == "__main__":
    main()