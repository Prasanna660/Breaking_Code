import breaking_backend as backend
import os
import streamlit as st

# Streamlit UI components

st.sidebar.title("GitHub Repository Analyzer")
url = st.sidebar.text_input("Enter the GitHub repository URL:", None)

uname_and_reponame = backend.get_username_and_repo_from_url(url)

st.markdown("""
### Instructions
1. Enter the GitHub repository URL in the input box.
2. Click the 'Generate Report' button to process the repository and generate reports.
3. Select a report from the dropdown to view its contents.
""")

# Button to generate new report
if st.sidebar.button("Generate Report"):
    if url:
        with st.spinner('Generating Report...'):
            try:
                files = backend.process(url)
                st.success("Report Generated Successfully")
                st.write(f"""Report saved in: ./reports_generated/{uname_and_reponame}""")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Listing available reports in the sidebar
reports_dir = f"""./reports_generated/{uname_and_reponame}"""

def get_all_files(root,files=None):
    if(files==None):
        files=[]
    items = os.listdir(root)
    for item in items:
        if(os.path.isdir(f"{root}/{item}")):
            get_all_files(f"{root}/{item}",files)
        else:
            files.append(f"{root}/{item}")
    return [("/").join(file.split("/")[4:]) for file in files]

reports_list = get_all_files(reports_dir)
report_file = st.sidebar.selectbox("Select a report to view:", reports_list)

# Displaying the selected Markdown report
if report_file:
    with open(f"{reports_dir}/{report_file}", 'r', encoding='utf-8') as f:
        report_content = f.read()
        st.markdown(report_content, unsafe_allow_html=True)

