# ResuMateAI 📄✨

**Optimize your resume for ATS with AI-driven insights and personalized feedback!**

ResuMateAI is a powerful Streamlit application that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS) using artificial intelligence. Get instant feedback, skill gap analysis, and generate optimized resumes tailored to specific job descriptions.

## 🚀 Features

- **Job Description Analysis**: Get insights on what employers are looking for
- **Skills Gap Analysis**: Identify missing skills and competencies
- **Resume Match Percentage**: See how well your resume matches the job requirements
- **ATS Compatibility Check**: Ensure your resume passes ATS filters
- **Resume Feedback**: Get detailed suggestions for improvement
- **Optimized Resume Generation**: Generate an AI-enhanced version of your resume
- **Cover Letter Generator**: Create personalized cover letters for job applications

## 📋 Prerequisites

Before running the application, make sure you have:

- Python 3.8 or higher
- Required Python packages (see requirements below)
- API access for AI services (configure in your environment)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/resumateai.git
   cd resumateai
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   # Create a .env file and add your API keys
   cp .env.example .env
   # Edit .env with your actual API keys
   ```

## 📦 Dependencies

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit
google-generativeai
python-dotenv
pdf2image
fpdf
PyPDF2
```

## 🏃‍♂️ Usage

1. **Start the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:8501
   ```

3. **Using the application:**
   - Paste the job description in the text area
   - Upload your resume in PDF format
   - Use the analysis buttons to get insights:
     - **Job Description Insights**: Understand key requirements
     - **Skills Gap Analysis**: Find missing skills
     - **Resume Percentage Match**: Get compatibility score
     - **ATS Compatibility Check**: Ensure ATS compliance
     - **Resume Feedback**: Receive improvement suggestions
     - **Generate Optimized Resume**: Create enhanced resume
     - **Generate Cover Letter**: Create personalized cover letter

## 📁 Project Structure

```
resumateai/
│
├── app.py                 # Main Streamlit application
├── prompts.py            # AI prompts and templates
├── utils.py              # Utility functions (PDF handling, API calls)
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# API Configuration
GEMINI_API_KEY=your_gemini_api_key_here

```

📸 Screenshots
Main Interface
<img width="1919" height="812" alt="image" src="https://github.com/user-attachments/assets/d223ff25-2767-44de-8313-a5c408b293b5" />
Clean and intuitive interface for job description input and resume upload
Analysis Options
<img width="1919" height="786" alt="image" src="https://github.com/user-attachments/assets/a8b90eae-10f8-40aa-8651-1dc5d6e95e51" />
Comprehensive set of AI-powered analysis tools in an expandable panel
Generated Insights
<img width="1919" height="830" alt="image" src="https://github.com/user-attachments/assets/c3f121e6-6e2c-4839-93f2-d2ee7876192f" />
Example of AI-generated resume feedback and recommendations

## 🎯 Key Functions

### `extractPDF(uploaded_file)`
Extracts text content from uploaded PDF files.

### `sendRequest(job_description, resume_content, prompt)`
Sends requests to AI services for analysis and generation.

### `createPDF(content, filename)`
Generates optimized PDF files from AI responses.

## 🐛 Troubleshooting

### Common Issues

**Issue**: "API key not found"
**Solution**: Check your `.env` file and ensure API keys are properly set

**Issue**: "PDF extraction failed"
**Solution**: Ensure the PDF is not password-protected and contains readable text

**Issue**: "Streamlit not found"
**Solution**: Make sure you're in the correct virtual environment and have installed dependencies



