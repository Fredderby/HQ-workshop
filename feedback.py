import streamlit as st
from datetime import datetime
from connect import cred # Assuming this contains your credentials function

def hq_feedback():
    """
    Professional questionnaire for Workplace Ethics workshop feedback
    """
    class WorkshopQuestionnaire:
        def __init__(self):
            self.client = None
            self.worksheet = None
            self.initialize_credentials()
            
        def initialize_credentials(self):
            """Initialize Google Sheets credentials"""
            try:
                self.client = cred()
                spreadsheet = self.client.open("HQ-feedback")
                self.worksheet = spreadsheet.worksheet("workshop")
                st.success("✅ Network Active!")
            except Exception as e:
                st.error(f"❌ Connection failed: {str(e)}")
        
        def format_department_name(self, dept_name):
            """Format department name to proper case"""
            if dept_name:
                return dept_name.title()
            return dept_name
        
        def validate_form(self, department, date, knowledge, expectations, wants):
            """Validate form inputs"""
            if not department.strip():
                st.error("Please enter your Department/Unit/Ministry")
                return False
            if not date:
                st.error("Please select today's date")
                return False
            if not knowledge.strip():
                st.error("Please share what you know about workplace ethics")
                return False
            if not expectations.strip():
                st.error("Please share your expectations")
                return False
            return True
        
        def submit_feedback(self, form_data):
            """Submit feedback to Google Sheets"""
            try:
                # Prepare data for submission
                submission_data = [
                    form_data['department'],
                    form_data['date'].strftime("%Y-%m-%d"),
                    form_data['knowledge'],
                    form_data['wants'],
                    form_data['expectations'],
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ]
                
                # Append to worksheet
                self.worksheet.append_row(submission_data)
                return True
            except Exception as e:
                st.error(f"Submission failed: {str(e)}")
                return False
        
        def render_questionnaire(self):
            """Render the complete questionnaire"""
            
            # Personal Information Section
            with st.container(border=True):
                st.markdown("### 📋 Personal Information")
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    department = st.text_input(
                        "Department/Unit/Ministry *",
                        placeholder="e.g., Human Resources, Finance Department",
                        help="Please enter your official department name"
                    )
                
                with col2:
                    today_date = st.date_input(
                        "Today's Date *",
                        value=datetime.now(),
                        max_value=datetime.now(),
                        help="Select today's date"
                    )
            
            # Workshop Content Section
            with st.container(border=True):
                st.markdown("### 💭 Workshop Insights")
                
                current_knowledge = st.text_area(
                    "What do you know about workplace ethics? *",
                    height=120,
                    placeholder="Share your current understanding and experience with workplace ethics...",
                    help="Describe your existing knowledge about workplace ethics"
                )
                
                want_to_know = st.text_area(
                    "What do you want to know about workplace ethics?",
                    height=120,
                    placeholder="What specific aspects of workplace ethics are you interested in learning?",
                    help="List topics or questions you'd like addressed in the workshop"
                )
            
            # Expectations Section
            with st.container(border=True):
                st.markdown("### 🎯 Expectations")
                
                expectations = st.text_area(
                    "What is your expectation? *",
                    height=120,
                    placeholder="What do you hope to gain from this workshop? What outcomes are you expecting?",
                    help="Share your expectations for the workshop content and outcomes"
                )
            
            # Submission Section
            with st.container(border=True):
                st.markdown("### 📤 Submission")
                
                st.markdown("**Required fields are marked with ***")
                
                if st.button("Submit Feedback", type="primary", use_container_width=True):
                    # Validate form
                    if not self.validate_form(department, today_date, current_knowledge, expectations, want_to_know):
                        return
                    
                    # Format department name
                    formatted_department = self.format_department_name(department)
                    
                    # Prepare form data
                    form_data = {
                        'department': formatted_department,
                        'date': today_date,
                        'knowledge': current_knowledge,
                        'wants': want_to_know,
                        'expectations': expectations
                    }
                    
                    # Submit data
                    if self.submit_feedback(form_data):
                        st.success("🎉 Thank you for your valuable feedback! Your responses have been successfully submitted.")
                        
                        # Show summary
                        with st.expander("Review Your Submission"):
                            st.write(f"**Department:** {formatted_department}")
                            st.write(f"**Date:** {today_date.strftime('%B %d, %Y')}")
                            st.write(f"**Current Knowledge:** {current_knowledge}")
                            if want_to_know.strip():
                                st.write(f"**Learning Goals:** {want_to_know}")
                            st.write(f"**Expectations:** {expectations}")
                    else:
                        st.error("❌ There was an error submitting your feedback. Please try again.")
    
    # Initialize and render the questionnaire
    questionnaire = WorkshopQuestionnaire()
    questionnaire.render_questionnaire()

# Note: Make sure to import and call this function from your main Streamlit app
# Example: 
# from questionnaire import hq_feedback
# hq_feedback()