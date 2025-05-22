import streamlit as st
from debate_bot_simple import DebateMentor
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
    
    # Sidebar for settings and tips
    st.sidebar.title("💡 Debate Tips")
    st.sidebar.markdown("---")
    
    tips = [
        "🎯 Start with a clear thesis statement",
        "📊 Support claims with evidence",
        "🤔 Address counterarguments",
        "🎭 Avoid personal attacks",
        "📝 Use logical reasoning",
        "🔍 Be specific with examples"
    ]
    
    for tip in tips:
        st.sidebar.markdown(f"• {tip}")
    
    # Main interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 Your Debate Position")
        
        # Topic input
        topic = st.text_input(
            "💭 Enter a debate topic:",
            placeholder="e.g., Social media should be regulated by governments",
            help="Enter any controversial topic you'd like to debate about"
        )
        
        # Stance selection
        stance = st.radio(
            "🎯 Choose your stance:",
            ["For", "Against"],
            help="Select whether you're arguing FOR or AGAINST the topic"
        )
        
        # User argument input
        user_argument = st.text_area(
            "✍️ Enter your argument:",
            placeholder="Write your best argument here... Include evidence, reasoning, and examples to make it stronger.",
            height=180,
            help="Present your strongest reasoning for your chosen position"
        )
        
        # Analysis button
        analyze_button = st.button("🔍 Analyze My Argument", type="primary", use_container_width=True)
        
        # Argument strength preview
        if user_argument:
            strength = mentor.analyze_argument_strength(user_argument)
            st.markdown("### 📊 Quick Stats")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Words", strength['word_count'])
            with col_b:
                st.metric("Evidence", strength['evidence_indicators'])
            with col_c:
                st.metric("Reasoning", strength['reasoning_indicators'])
    
    with col2:
        st.header("🤖 AI Analysis & Feedback")
        
        if analyze_button and topic and user_argument:
            with st.spinner("🧠 Analyzing your argument..."):
                # Simulate processing time for better UX
                time.sleep(1)
                
                # Get bot's stance (opposite of user)
                bot_stance = "Against" if stance == "For" else "For"
                
                # Generate bot's argument for their stance
                bot_argument = mentor.generate_stance_argument(topic, bot_stance)
                
                # Analyze user's argument for fallacies
                fallacy_analysis = mentor.detect_fallacies(user_argument)
                
                # Generate counterargument
                counterargument = mentor.generate_counterargument(topic, user_argument, stance)
                
                # Display results
                st.subheader(f"🎯 AI's {bot_stance} Position")
                st.info(f"**{bot_stance} {topic}:**\n\n{bot_argument}")
                
                st.subheader("🔍 Logical Fallacy Check")
                if fallacy_analysis['has_fallacies']:
                    st.warning("⚠️ **Potential logical fallacies detected:**")
                    for i, fallacy in enumerate(fallacy_analysis['fallacies'], 1):
                        st.markdown(f"**{i}. {fallacy['type']}**")
                        st.markdown(f"   *{fallacy['explanation']}*")
                else:
                    st.success("✅ **No obvious logical fallacies detected!**")
                    st.markdown("Your argument appears to be logically sound.")
                
                st.subheader("💥 Counterargument Challenge")
                st.error(f"**Challenging your {stance} position:**\n\n{counterargument}")
                
                # Improvement suggestions
                st.subheader("📈 How to Improve")
                suggestions = mentor.get_improvement_suggestions(user_argument, fallacy_analysis)
                
                for i, suggestion in enumerate(suggestions, 1):
                    st.markdown(f"**{i}.** {suggestion}")
                
                # Overall assessment
                strength = mentor.analyze_argument_strength(user_argument)
                total_indicators = strength['evidence_indicators'] + strength['reasoning_indicators'] + strength['balance_indicators']
                
                if total_indicators >= 3:
                    assessment = "Strong"
                    color = "green"
                elif total_indicators >= 1:
                    assessment = "Moderate"
                    color = "orange"
                else:
                    assessment = "Needs Work"
                    color = "red"
                
                st.markdown("---")
                st.markdown(f"**Overall Assessment:** :{color}[{assessment}]")
        
        elif analyze_button:
            st.warning("⚠️ Please fill in both the topic and your argument to get analysis!")
        
        else:
            st.markdown("### 🎯 How It Works")
            st.markdown("""
            1. **Enter a topic** you want to debate
            2. **Choose your stance** (For/Against)  
            3. **Write your argument** with reasoning
            4. **Get instant feedback** on:
               - Logical fallacies
               - Counter-arguments
               - Improvement suggestions
            """)
    
    # Footer with example topics
    st.markdown("---")
    st.markdown("### 💡 Try These Example Topics")
    
    example_topics = [
        "Artificial intelligence will replace most human jobs",
        "Climate change requires immediate government intervention", 
        "Social media platforms should fact-check all content",
        "Universal basic income should be implemented globally",
        "Genetic engineering of humans should be allowed",
        "Remote work is better than office work",
        "Standardized testing should be abolished in schools"
    ]
    
    # Display examples in columns
    cols = st.columns(3)
    for i, example in enumerate(example_topics):
        col_idx = i % 3
        with cols[col_idx]:
            if st.button(f"📝 {example}", key=f"example_{i}", use_container_width=True):
                st.rerun()
    
    # Additional info
    st.markdown("---")
    st.markdown("### ℹ️ About Debate Mentor")
    with st.expander("Learn more about the analysis"):
        st.markdown("""
        **Fallacy Detection:** Uses pattern matching to identify common logical errors
        
        **Argument Analysis:** Evaluates structure, evidence, and reasoning quality
        
        **Counterarguments:** Generates opposing viewpoints to challenge your thinking
        
        **Suggestions:** Provides specific, actionable feedback for improvement
        
        This tool is designed to help you become a better debater by practicing critical thinking and argument construction.
        """)

if __name__ == "__main__":
    main()