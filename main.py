from itertools import zip_longest
import streamlit as st
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
openapi_key = st.secrets["OPENAI_API_KEY"]

# Set streamlit page configuration
# Set streamlit page configuration
st.set_page_config(page_title="Portfolio-Bot")
st.title("Portfolio-Bot")

# Initialize session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # Store AI generated responses

if 'past' not in st.session_state:
    st.session_state['past'] = []  # Store past user inputs

if 'entered_prompt' not in st.session_state:
    st.session_state['entered_prompt'] = ""  # Store the latest user input

# Initialize the ChatOpenAI model
chat = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-3.5-turbo",
    openai_api_key=openapi_key, 
    max_tokens=100
)


def build_message_list():
    """
    Build a list of messages including system, human and Ai chatbot of Portfolio-Bot it company messages.
    """
    # Start zipped_messages with the SystemMessage
    zipped_messages = [SystemMessage(
        # content="You are a helpful AI assistant talking with a human. If you do not know an answer, just say 'I don't know', do not make up an answer.")]
        content = """ when the user ask  hi  tell him Welcome to the Portfolio-Bot developed by Khalid Kifayat, you can ask any question about khalid kifayat. His education, skills, experience, projects etc I am here to assist you as a knowledgeable consultant. 

---
**About Portfolio-Bot:**
Portfolio-Bot is digital chatbot which answer questions about khalid kifayat, his education, his skills, his experience, projects delivered.
---
**About Khalid Kifayat:**
Hello, I'm Khalid kifayat, Skillful Ai-Engineer with working experience in Cloud computing (AWS, GCP), Infrastructure deployment, testing, monitoring, scripting, automation, Version control, documentation & system's support.
I also work as a proficient AI-chatbot developer in Google Dialogflow & Amazon Alexa with a keen eye for design, coding finesse, and a knack for creating intelligent chatbots using Rule based and Generative AI mechanism's, I bring a holistic approach to crafting dynamic and user-centric digital solutions
---
**Education**
1. Master's in Computer Sciences - Iqra University Karachi - 2004.
2. Bachelor's in Computer Sciences - University of Peshawar - 2001
---
**Skills**
1. Git, GitHub, GitLab for version control and collaboration.
2. SonarQube/JFrog for code testing.
3. CI/CD: Jenkins ArgoCD, GitLab CI/CD for automation.
4. Containerization: Docker and Kubernetes.
5. Infrastructure as Code: Terraform, Ansible, Cloud-Formation
6. Monitoring: AWS Cloud-Watch, Google Cloud Ops-Agent Monitoring, or tools like Prometheus Grafana.
7. Security: IAM, Cloud Armor, Active Directory (AD)
---
**Cloud/DevOps Projects**
1. CICD Pipeline for Java Application to deploy on Kubernetes Cluster using Jenkins.
2. Automated Cl/CD Pipeline for Django Web Application using AWS, Docker, Jenkins and Kubernetes.
3. Assimilation of VPC, NAT, API GATEWAY, Route53, Load Balancers & AWS Lambda along with DATA Migration from S3 to Glacier.
4. Manage, Secure, Validate, Debug, Monitor & Prevent Misconfiguration of Kubernetes.
5. MongoExpress/MongoDB Application deployment using Kubernetes.
6. Deploying App using GiT-Maven-Jenkins & Tomcat Server.
---
**Ai Chatbot Projects:**
1. https://chatbot-saylani.netlify.app/
2. https://daraz-ai.netlify.app/ 
---
**Communication skills**
khalid kifayat possesses the following skills,
1. Effective communicator
2. Teamwork & Leadership
3. Customer focused
4. Active licensing
---
**Job Experience**
1. IT Technical Analyst (Pakistan Tobacco Company (PTC) l Location: Akora Khattak Factory, KPK, Pakistan (Client: HRSPL)) July 19 - Sept 20
2. IT Officer, Rural Livelihood & Community Infrastructure Project (RLCIP) l Location: Peshawar, Pakistan , May 2013 - Mar 2018
3. IT Admin, Area Development Project for Frontier Regions (ADP-FRs) l Location: Peshawar, Pakistan, July 2010 - Apr 2013
4. IT Admin, South FATA Development Project (SFDP) l Location: Peshawar, Pakistan, June 2007 - June 2010
5. Assistant Network Engineer, Warid Telecom (Telecom Company) l Location: Peshawar, Pakistan, Oct 2004 - May 2007

Thank you for choosing khalid kifayat Portfolio-Bot. If you have any questions or require assistance, feel free to ask! """
    )]


    # Zip together the past and generated messages
    for human_msg, ai_msg in zip_longest(st.session_state['past'], st.session_state['generated']):
        if human_msg is not None:
            zipped_messages.append(HumanMessage(
                content=human_msg))  # Add user messages
        if ai_msg is not None:
            zipped_messages.append(
                AIMessage(content=ai_msg))  # Add AI messages

    return zipped_messages


def generate_response():
    """
    Generate AI response using the ChatOpenAI model.
    """
    # Build the list of messages
    zipped_messages = build_message_list()

    # Generate response using the chat model
    ai_response = chat(zipped_messages)

    return ai_response.content


# Define function to submit user input
def submit():
    # Set entered_prompt to the current value of prompt_input
    st.session_state.entered_prompt = st.session_state.prompt_input
    # Clear prompt_input
    st.session_state.prompt_input = ""


# Create a text input for user
st.text_input('YOU: ', key='prompt_input', on_change=submit)


if st.session_state.entered_prompt != "":
    # Get user query
    user_query = st.session_state.entered_prompt

    # Append user query to past queries
    st.session_state.past.append(user_query)

    # Generate response
    output = generate_response()

    # Append AI response to generated responses
    st.session_state.generated.append(output)


# Display the chat history
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        # Display AI response
        message(st.session_state["generated"][i], key=str(i))
        # Display user message
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')








# import streamlit as st

# # Set streamlit page configuration
# st.set_page_config(page_title="Hope to Skill ChatBot")
# st.title("AI Mentor")

# # Create a sidebar for user information (optional)
# st.sidebar.title("User Information")
# st.sidebar.write("Name: Muhammad Abdullah")
# st.sidebar.write("Age: 21")
# st.sidebar.write("Location: Upper Dir, Khyber Pakhtunkhwa")
# st.sidebar.write("Education: Computer Science")

# # Create a text input for user
# st.text_input('YOU: ', key='prompt_input')

# # Display the chat history
# if st.session_state['generated']:
#     for i in range(len(st.session_state['generated'])-1, -1, -1):
#         # Display AI response
#         st.write(st.session_state["generated"][i])
#         # Display user message
#         st.write(st.session_state['past'][i])