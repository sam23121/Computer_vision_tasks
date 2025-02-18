import streamlit as st
import requests
import base64
import imghdr
from PIL import Image
import io
from agentic_object_detection.main import count_food_items_in_image

st.title('Food Item Composition Analyzer')
st.write('Upload an image to analyze the composition of peas, pearl onions and mushrooms.')


uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Process the image using the local function
    with st.spinner('Analyzing image...'):
        # Save the uploaded image to a temporary file
        try:
            temp_image_path = "assets/temp_uploaded_image.jpg"
            image.save(temp_image_path)
        except Exception as e:
            st.error(f"Error saving image: {e}")
            pass
        
        # Use the local function to count food items and get the annotated image
        result = count_food_items_in_image(temp_image_path)
        
        # Get total count of all items
        total_items = result['peas'] + result['pearl_onions'] + result['mushrooms']
        
        # Calculate percentages
        pea_percentage = (result['peas'] / total_items) * 100
        onion_percentage = (result['pearl_onions'] / total_items) * 100
        mushroom_percentage = (result['mushrooms'] / total_items) * 100
        
        # Display results
        st.subheader('Composition of items:')
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Peas", f"{pea_percentage:.1f}%")
        with col2:
            st.metric("Pearl Onions", f"{onion_percentage:.1f}%")
        with col3:
            st.metric("Mushrooms", f"{mushroom_percentage:.1f}%")
        
        # Display the annotated image
        st.subheader('Annotated Image:')
        st.image(result['annotated_image'], caption='Annotated Image with Detections', use_column_width=True)
        
        # Display raw response
        if st.checkbox('Show raw response'):
            st.json(result)
