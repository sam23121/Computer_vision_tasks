import streamlit as st
import requests
import base64
import imghdr
from PIL import Image
import io

st.title('Food Item Composition Analyzer')
st.write('Upload an image to analyze the composition of peas, pearl onions and mushrooms.')

url = "https://ig8qqgy-webendpoint.sandbox.landing.ai/inference"

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Process the image
    image_data = uploaded_file.getvalue()
    image_format = imghdr.what(None, h=image_data)
    if image_format is None:
        st.error("Could not determine the image format")
    else:
        base64_image = base64.b64encode(image_data).decode('utf-8')
        
        base64_image_formatted = f"data:image/{image_format};base64,{base64_image}"
        payload = { "image_path": base64_image_formatted }
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic Mml4eWM2ano1Mzc5bjM2ZzJlbXA4OmdIdndxZVZuMnVvZFVPcGFDQURBTUFBYUY0MTR3eXQ4"
        }
        
        with st.spinner('Analyzing image...'):
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                st.success('Analysis complete!')
                
                # Get total count of all items
                result = response.json()
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
                
                # Display raw response
                if st.checkbox('Show raw response'):
                    st.json(response.json())
            else:
                st.error(f'Error: {response.status_code}')
                st.json(response.json())
