import streamlit as st
from debate_bot import DebateMentor
import time

# Initialize the debate mentor
@st.cache_resource
def load_debate_mentor():
    return DebateMentor()

def main():
    st.set_page_config(
        page_title="Debate Mentor",
        page_icon="🗣️",
        layout="wide"
    )
    
    st.title("🗣️ Debate Mentor")
    st.markdown("*Improve your debating skills with AI-powered analysis and counterarguments*")
    
    # Initialize debate mentor
    mentor = load_debate_mentor()
    
    # Sidebar for settings
    st.sidebar.title("⚙️ Settings")
    st.sidebar.markdown("---")
    
    # Main interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 Your Debate")
        
        # Topic input
        topic = st.text_input(
            "Enter a debate topic:",
            placeholder="e.g., Social media should be regulated by governments",
            help="Enter any controversial topic you'd like to debate"
        )
        
        # Stance selection
        stance = st.radio(
            "Choose your stance:",
            ["For", "Against"],
            help="Select whether you're arguing FOR or AGAINST the topic"
        )
        
        # User argument input
        user_argument = st.text_area(
            "Enter your argument:",
            placeholder="Write your argument here...",
            height=150,
            help="Present your best argument for your chosen stance"
        )
        
        # Analysis button
        analyze_button = st.button("🔍 Analyze My Argument", type="primary")
    
    with col2:
        st.header("🤖 AI Analysis")
        
        if analyze_button and topic and user_argument:
            with st.spinner("Analyzing your argument..."):
                # Get bot's stance (opposite of user)
                bot_stance = "Against" if stance == "For" else "For"
                
                # Generate bot's argument for their stance
                bot_argument = mentor.generate_stance_argument(topic, bot_stance)
                
                # Analyze user's argument for fallacies
                fallacy_analysis = mentor.detect_fallacies(user_argument)
                
                # Generate counterargument
                counterargument = mentor.generate_counterargument(topic, user_argument, stance)
                
                # Display results
                st.subheader(f"🎯 Bot's {bot_stance} Argument")
                st.info(bot_argument)
                
                st.subheader("🔍 Fallacy Analysis")
                if fallacy_analysis['has_fallacies']:
                    st.warning("⚠️ Potential logical fallacies detected:")
                    for fallacy in fallacy_analysis['fallacies']:
                        st.write(f"• **{fallacy['type']}**: {fallacy['explanation']}")
                else:
                    st.success("✅ No obvious logical fallacies detected!")
                
                st.subheader("💡 Counterargument")
                st.error(f"**Counter to your {stance} position:**\n\n{counterargument}")
                
                # Improvement suggestions
                st.subheader("📈 Suggestions for Improvement")
                suggestions = mentor.get_improvement_suggestions(user_argument, fallacy_analysis)
                for suggestion in suggestions:
                    st.write(f"• {suggestion}")
        
        elif analyze_button:
            st.warning("Please fill in both the topic and your argument!")
    
    # Footer with instructions
    st.markdown("---")
    st.markdown("### 📖 How to Use")
    st.markdown("""
    1. **Enter a debate topic** - Choose any controversial subject
    2. **Pick your stance** - Are you arguing FOR or AGAINST?
    3. **Write your argument** - Present your best reasoning
    4. **Get AI analysis** - Receive fallacy detection, counterarguments, and suggestions
    """)
    
    # Example topics
    st.markdown("### 💡 Example Topics")
    example_topics = [
        "Artificial intelligence will replace most human jobs",
        "Climate change requires immediate government intervention",
        "Social media platforms should fact-check all content",
        "Universal basic income should be implemented globally",
        "Genetic engineering of humans should be allowed"
    ]
    
    cols = st.columns(len(example_topics))
    for i, example in enumerate(example_topics):
        if cols[i].button(f"Use: {example[:30]}...", key=f"example_{i}"):
            st.session_state.topic_input = example

if __name__ == "__main__":
    main()