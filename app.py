import streamlit as st
st.title("The Identity Echo Interface")
st.write("Enter your name and what you intend to trasmit")
user_name=st.text_input("Enter your name")
user_msg=st.text_input("Please enter the message to transmit")
if st.button("Transmit"):
  if not user_name.strip():
    st.error("Please Provide your name")
  elif not user_msg.strip():
    st.error("Please provide the message to be transmitted")
  else:
    st.success(
            f"Transmission successful! Greetings, {user_name}. "
            f"We received your message: {user_message}"
        )
        character_count = len(user_message)
        token_count = character_count / 4

        st.info(
            f"System Check: Your message will consume approximately "
            f"{token_count:.2f} tokens from our context window."
        )
