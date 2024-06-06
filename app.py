import streamlit as st
import os
import cv2

# Function to load and display an image
def load_and_display_image(image_path, title):
    image = cv2.imread(image_path)
    st.subheader(title)
    st.image(image, caption=title, use_column_width=True)

# Streamlit App
def main():
    st.set_page_config(layout="wide")  # Set the layout to wide

    st.title("Land Change Detection ")

    demo_folder = "DEMO"
    if not os.path.exists(demo_folder):
        st.error(f"Demo folder not found: {demo_folder}")
        return

    instance_folders = [f for f in os.listdir(demo_folder) if os.path.isdir(os.path.join(demo_folder, f))]

    if not instance_folders:
        st.warning("No instance folders found in the demo folder.")
        return

    for instance_folder in instance_folders:
        instance_path = os.path.join(demo_folder, instance_folder)
        after_path = os.path.join(instance_path, "after.png")
        before_path = os.path.join(instance_path, "before.png")
        predicted_path = os.path.join(instance_path, "predicted.png")
        result_path = os.path.join(instance_path, "result.png")

        st.header(f"Processing Instance: {instance_folder}")

        # Create four columns for "before", "after", "predicted", and "result" images
        col1, col2, col3, col4 = st.columns(4)

        # Display "before" image in the first column
        with col1:
            load_and_display_image(before_path, "Before Image")

        # Display "after" image in the second column
        with col2:
            load_and_display_image(after_path, "After Image")

        # Display the predicted image in the third column
        with col3:
            load_and_display_image(predicted_path, "Predicted Segmentation")

        # Display the result image in the fourth column
        with col4:
            if os.path.exists(result_path):
                load_and_display_image(result_path, "Result Image")
            else:
                st.warning("Result image not found.")

        st.write("---")  # Add a horizontal line between instances

if __name__ == "__main__":
    main()
