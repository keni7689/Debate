"""
Utility functions for the Debate Mentor application.
"""

import re
import string
from typing import List, Dict

def clean_text(text: str) -> str:
    """Clean and normalize text input."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Strip leading/trailing whitespace
    text = text.strip()
    return text

def extract_keywords(text: str, min_length: int = 3) -> List[str]:
    """Extract meaningful keywords from text."""
    # Convert to lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split into words and filter
    words = text.split()
    
    # Common stop words to exclude
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
        'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 
        'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
        'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 
        'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'its',
        'our', 'their'
    }
    
    # Filter words
    keywords = [
        word for word in words 
        if len(word) >= min_length and word not in stop_words
    ]
    
    return list(set(keywords))  # Remove duplicates

def calculate_argument_strength(argument: str) -> Dict[str, int]:
    """Calculate basic metrics for argument strength."""
    # Word count
    word_count = len(argument.split())
    
    # Sentence count
    sentence_count = len(re.split(r'[.!?]+', argument))
    
    # Evidence indicators
    evidence_words = ['research', 'study', 'data', 'statistics', 'evidence', 'proof']
    evidence_count = sum(1 for word in evidence_words if word in argument.lower())
    
    # Reasoning indicators
    reasoning_words = ['because', 'since', 'therefore', 'thus', 'consequently', 'as a result']
    reasoning_count = sum(1 for word in reasoning_words if word in argument.lower())
    
    # Counterargument acknowledgment
    counter_words = ['however', 'although', 'while', 'despite', 'nevertheless', 'but']
    counter_count = sum(1 for word in counter_words if word in argument.lower())
    
    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'evidence_indicators': evidence_count,
        'reasoning_indicators': reasoning_count,
        'counter_acknowledgment': counter_count
    }

def format_fallacy_name(fallacy_name: str) -> str:
    """Format fallacy names for display."""
    # Replace underscores with spaces and title case
    formatted = fallacy_name.replace('_', ' ').title()
    
    # Special cases for better readability
    replacements = {
        'Ad Hominem': 'Ad Hominem Attack',
        'Strawman': 'Straw Man Fallacy',
        'False Dichotomy': 'False Dichotomy'
    }
    
    return replacements.get(formatted, formatted)

def generate_topic_suggestions(keywords: List[str]) -> List[str]:
    """Generate related topic suggestions based on keywords."""
    topic_templates = [
        "Should {keyword} be regulated by government?",
        "Is {keyword} more beneficial than harmful?",
        "Does {keyword} threaten traditional values?",
        "Should {keyword} be available to everyone?",
        "Is {keyword} a fundamental right?"
    ]
    
    suggestions = []
    for keyword in keywords[:3]:  # Limit to first 3 keywords
        for template in topic_templates[:2]:  # Limit to 2 templates per keyword
            suggestion = template.format(keyword=keyword)
            suggestions.append(suggestion)
    
    return suggestions

def validate_input(topic: str, argument: str) -> Dict[str, bool]:
    """Validate user input."""
    validation = {
        'topic_valid': len(topic.strip()) >= 10,
        'argument_valid': len(argument.strip()) >= 20,
        'topic_error': '',
        'argument_error': ''
    }
    
    if not validation['topic_valid']:
        validation['topic_error'] = "Topic should be at least 10 characters long"
    
    if not validation['argument_valid']:
        validation['argument_error'] = "Argument should be at least 20 characters long"
    
    return validation

def get_debate_tips() -> List[str]:
    """Get random debate tips for users."""
    tips = [
        "Start with a clear thesis statement that outlines your main position.",
        "Use the PEEL structure: Point, Evidence, Explanation, Link.",
        "Always consider and address potential counterarguments.",
        "Support your claims with credible sources and evidence.",
        "Use logical reasoning rather than emotional appeals.",
        "Be respectful and focus on ideas, not personal attacks.",
        "Practice active listening to understand opposing viewpoints.",
        "Use specific examples to illustrate your points.",
        "Keep your arguments concise and well-organized.",
        "End with a strong conclusion that reinforces your main points."
    ]
    
    import random
    return random.sample(tips, 3)

def analyze_argument_complexity(argument: str) -> str:
    """Analyze the complexity level of an argument."""
    metrics = calculate_argument_strength(argument)
    
    # Simple scoring system
    score = 0
    
    if metrics['word_count'] > 100:
        score += 2
    elif metrics['word_count'] > 50:
        score += 1
    
    if metrics['evidence_indicators'] > 0:
        score += 2
    
    if metrics['reasoning_indicators'] > 0:
        score += 2
    
    if metrics['counter_acknowledgment'] > 0:
        score += 1
    
    # Determine complexity level
    if score >= 6:
        return "Advanced"
    elif score >= 3:
        return "Intermediate"
    else:
        return "Beginner"