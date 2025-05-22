# 🗣️ Debate Mentor

An AI-powered chatbot that helps users improve their debating skills through stance analysis, logical fallacy detection, and real-time counterarguments.

## 🎯 Features

- **Stance-Based Arguments** : AI takes opposing positions and generates structured arguments
- **Logical Fallacy Detection** : Identifies common fallacies like ad hominem, straw man, false dichotomy, etc.
- **Real-Time Counterarguments** : Generates intelligent responses to challenge your reasoning
- **Improvement Suggestions** : Provides actionable feedback to strengthen your arguments
- **User-Friendly Interface** : Clean Streamlit web interface

## 🛠️ Tech Stack

- **Frontend** : Streamlit
- **AI/NLP** : Hugging Face Transformers (Microsoft DialoGPT-small)
- **Fallacy Detection** : Rule-based pattern matching
- **Language** : Python 3.8+

## 📁 Project Structure

```
debate_mentor/
├── app.py                  # Streamlit web interface
├── debate_bot.py           # Core debate logic and AI models
├── utils.py                # Helper functions and utilities
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step-by-Step Installation

1. **Clone or Download the Project**

   ```bash
   git clone <repository-url>
   cd debate_mentor
   ```

   _Or download and extract the ZIP file_

2. **Create a Virtual Environment (Recommended)**

   ```bash
   python -m venv debate_env

   # On Windows:
   debate_env\Scripts\activate

   # On macOS/Linux:
   source debate_env/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   streamlit run app.py
   ```

5. **Open Your Browser**

   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, visit the URL shown in your terminal

## 💡 How to Use

1. **Enter a Debate Topic**
   - Type any controversial subject (e.g., "Social media should be regulated by governments")
2. **Choose Your Stance**
   - Select either "For" or "Against" the topic
3. **Write Your Argument**
   - Present your best reasoning in the text area
4. **Get AI Analysis**
   - Click "Analyze My Argument" to receive:
     - The AI's opposing argument
     - Logical fallacy detection
     - Counterarguments to your position
     - Suggestions for improvement

## 📚 Example Topics to Try

- "Artificial intelligence will replace most human jobs"
- "Climate change requires immediate government intervention"
- "Social media platforms should fact-check all content"
- "Universal basic income should be implemented globally"
- "Genetic engineering of humans should be allowed"

## 🧠 AI Models Used

### Primary Model

- **Microsoft DialoGPT-small** : Lightweight conversational AI model from Hugging Face
- Size: ~117MB
- Purpose: Text generation for arguments and counterarguments
- Fallback: Rule-based generation if model fails to load

### Fallacy Detection

- **Rule-based Pattern Matching** : Custom regex patterns for detecting:
- Ad Hominem attacks
- Straw Man fallacies
- False Dichotomy
- Appeal to Emotion
- Hasty Generalization
- Slippery Slope

## 🔧 Troubleshooting

### Common Issues

1. **Model Loading Errors**
   - The app uses a fallback system if the AI model fails to load
   - Check your internet connection for initial model download
2. **Dependencies Issues**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt --force-reinstall
   ```
3. **Port Already in Use**
   ```bash
   streamlit run app.py --server.port 8502
   ```
4. **Memory Issues**
   - The DialoGPT-small model is lightweight (~117MB)
   - If you have <4GB RAM, close other applications

### Performance Tips

- **First Run** : Initial model download may take 1-2 minutes
- **Subsequent Runs** : Models are cached locally for faster loading
- **Response Time** : Analysis typically takes 2-5 seconds

## 🎓 Educational Features

### Logical Fallacies Detected

- **Ad Hominem** : Personal attacks instead of addressing arguments
- **Straw Man** : Misrepresenting opponent's position
- **False Dichotomy** : Presenting only two options when more exist
- **Appeal to Emotion** : Using feelings instead of logic
- **Hasty Generalization** : Broad conclusions from limited examples
- **Slippery Slope** : Assuming extreme consequences

### Improvement Suggestions

- Argument structure and length analysis
- Evidence and reasoning indicators
- Tone and emotional content evaluation
- Counterargument acknowledgment

## 📈 Future Enhancements

- Integration with larger language models
- More sophisticated fallacy detection
- Debate scoring system
- Historical argument tracking
- Multiplayer debate modes

## 🤝 Contributing

This is a beginner-friendly project! Areas for contribution:

- Additional fallacy patterns
- Better argument templates
- UI/UX improvements
- More sophisticated AI models
- Performance optimizations

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure all dependencies are installed correctly
3. Verify Python version compatibility (3.8+)

---

**Happy Debating! 🗣️**
