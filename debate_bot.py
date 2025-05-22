import re
import random
from typing import Dict, List
from transformers import pipeline
import warnings
warnings.filterwarnings("ignore")

class DebateMentor:
    def __init__(self):
        """Initialize the Debate Mentor with lightweight models."""
        self.text_generator = None
        try:
            # Try to use a lightweight text generation model
            from transformers import pipeline
            self.text_generator = pipeline(
                "text-generation",
                model="microsoft/DialoGPT-small",
                tokenizer="microsoft/DialoGPT-small",
                pad_token_id=50256,
                device=-1  # Force CPU usage
            )
        except Exception as e:
            # Fallback to rule-based generation if model fails
            print(f"Model loading failed: {e}")
            print("Using rule-based text generation as fallback")
            self.text_generator = None
        
        # Define logical fallacies patterns
        self.fallacy_patterns = {
            "ad_hominem": {
                "patterns": [
                    r"you are (stupid|dumb|ignorant|wrong)",
                    r"people like you",
                    r"typical (liberal|conservative)",
                    r"you don't understand",
                    r"you're just"
                ],
                "explanation": "Attacking the person rather than their argument"
            },
            "strawman": {
                "patterns": [
                    r"so you're saying",
                    r"what you really mean",
                    r"you want to",
                    r"your position is that"
                ],
                "explanation": "Misrepresenting opponent's argument to make it easier to attack"
            },
            "false_dichotomy": {
                "patterns": [
                    r"either.*or",
                    r"only two options",
                    r"you must choose",
                    r"there are only"
                ],
                "explanation": "Presenting only two options when more exist"
            },
            "appeal_to_emotion": {
                "patterns": [
                    r"think of the children",
                    r"how can you live with yourself",
                    r"this is heartbreaking",
                    r"imagine if"
                ],
                "explanation": "Using emotional manipulation instead of logical reasoning"
            },
            "hasty_generalization": {
                "patterns": [
                    r"all.*are",
                    r"every.*is",
                    r"always",
                    r"never"
                ],
                "explanation": "Making broad conclusions from limited examples"
            },
            "slippery_slope": {
                "patterns": [
                    r"if we allow.*then",
                    r"this will lead to",
                    r"next thing you know",
                    r"where does it end"
                ],
                "explanation": "Assuming one event will lead to extreme consequences"
            }
        }
        
        # Common debate argument templates
        self.argument_templates = {
            "For": [
                "Supporting {topic} is essential because it promotes {benefit} and addresses {problem}.",
                "The evidence clearly shows that {topic} leads to {positive_outcome} and improves {area}.",
                "From an ethical standpoint, {topic} is necessary to ensure {moral_good} and prevent {harm}.",
                "Research demonstrates that {topic} results in {statistic} improvement in {field}."
            ],
            "Against": [
                "Opposing {topic} is crucial because it prevents {negative_outcome} and protects {value}.",
                "The risks of {topic} far outweigh any potential benefits, particularly regarding {concern}.",
                "Historical evidence shows that {topic} has led to {negative_consequence} in {context}.",
                "From a practical perspective, {topic} is unfeasible due to {obstacle} and {limitation}."
            ]
        }
        
        # Common benefits, problems, outcomes for template filling
        self.template_fillers = {
            "benefit": ["equality", "innovation", "economic growth", "social progress", "individual freedom"],
            "problem": ["inequality", "inefficiency", "injustice", "environmental damage", "social discord"],
            "positive_outcome": ["increased prosperity", "better health outcomes", "reduced conflict", "enhanced security"],
            "negative_outcome": ["economic instability", "loss of privacy", "increased inequality", "social division"],
            "area": ["education", "healthcare", "the economy", "social welfare", "international relations"],
            "moral_good": ["justice", "fairness", "human rights", "dignity", "equality"],
            "harm": ["discrimination", "exploitation", "suffering", "injustice", "oppression"],
            "value": ["individual liberty", "democratic principles", "economic stability", "social cohesion"],
            "concern": ["privacy violations", "economic disruption", "unintended consequences", "abuse of power"],
            "field": ["public health", "economic indicators", "social metrics", "environmental measures"]
        }

    def generate_stance_argument(self, topic: str, stance: str) -> str:
        """Generate an argument for a given stance on a topic."""
        template = random.choice(self.argument_templates[stance])
        
        # Fill template with appropriate terms
        filled_template = template.format(
            topic=topic.lower(),
            benefit=random.choice(self.template_fillers["benefit"]),
            problem=random.choice(self.template_fillers["problem"]),
            positive_outcome=random.choice(self.template_fillers["positive_outcome"]),
            negative_outcome=random.choice(self.template_fillers["negative_outcome"]),
            area=random.choice(self.template_fillers["area"]),
            moral_good=random.choice(self.template_fillers["moral_good"]),
            harm=random.choice(self.template_fillers["harm"]),
            value=random.choice(self.template_fillers["value"]),
            concern=random.choice(self.template_fillers["concern"]),
            field=random.choice(self.template_fillers["field"]),
            statistic="significant",
            context="similar situations",
            obstacle="implementation challenges",
            limitation="resource constraints"
        )
        
        return filled_template

    def detect_fallacies(self, argument: str) -> Dict:
        """Detect logical fallacies in the given argument."""
        detected_fallacies = []
        argument_lower = argument.lower()
        
        for fallacy_name, fallacy_data in self.fallacy_patterns.items():
            for pattern in fallacy_data["patterns"]:
                if re.search(pattern, argument_lower):
                    detected_fallacies.append({
                        "type": fallacy_name.replace("_", " ").title(),
                        "explanation": fallacy_data["explanation"]
                    })
                    break  # Only add each fallacy type once
        
        return {
            "has_fallacies": len(detected_fallacies) > 0,
            "fallacies": detected_fallacies
        }

    def generate_counterargument(self, topic: str, user_argument: str, user_stance: str) -> str:
        """Generate a counterargument to the user's position."""
        opposite_stance = "Against" if user_stance == "For" else "For"
        
        # Start with a basic counterargument
        base_counter = self.generate_stance_argument(topic, opposite_stance)
        
        # Add specific rebuttals based on common argument patterns
        rebuttals = []
        
        if "benefit" in user_argument.lower() or "advantage" in user_argument.lower():
            rebuttals.append("However, these supposed benefits may be outweighed by significant hidden costs and unintended consequences.")
        
        if "research" in user_argument.lower() or "study" in user_argument.lower():
            rebuttals.append("While some studies support this view, conflicting research suggests different conclusions.")
        
        if "moral" in user_argument.lower() or "ethical" in user_argument.lower():
            rebuttals.append("This raises important ethical questions about competing moral principles and whose values should take precedence.")
        
        if "freedom" in user_argument.lower() or "rights" in user_argument.lower():
            rebuttals.append("We must balance individual freedoms with collective responsibilities and societal well-being.")
        
        # Combine base argument with specific rebuttals
        if rebuttals:
            return f"{base_counter} {random.choice(rebuttals)}"
        else:
            return f"{base_counter} Additionally, your argument doesn't fully address the potential negative implications and alternative perspectives on this issue."

    def get_improvement_suggestions(self, argument: str, fallacy_analysis: Dict) -> List[str]:
        """Provide suggestions for improving the argument."""
        suggestions = []
        
        # Fallacy-specific suggestions
        if fallacy_analysis["has_fallacies"]:
            suggestions.append("Address the logical fallacies identified to strengthen your reasoning")
            suggestions.append("Focus on evidence-based claims rather than emotional appeals or personal attacks")
        
        # General improvement suggestions based on argument analysis
        if len(argument.split()) < 50:
            suggestions.append("Expand your argument with more detailed reasoning and examples")
        
        if "because" not in argument.lower() and "since" not in argument.lower():
            suggestions.append("Add clear causal reasoning using words like 'because', 'since', or 'therefore'")
        
        if not any(word in argument.lower() for word in ["research", "study", "evidence", "data", "statistics"]):
            suggestions.append("Include references to research, data, or evidence to support your claims")
        
        if not any(word in argument.lower() for word in ["however", "although", "while", "despite"]):
            suggestions.append("Acknowledge counterarguments or limitations to show balanced thinking")
        
        if argument.count("!") > 2:
            suggestions.append("Use a more measured tone - avoid excessive exclamation points")
        
        # Always include at least one suggestion
        if not suggestions:
            suggestions.append("Consider adding more specific examples or case studies to illustrate your points")
            suggestions.append("Think about potential objections and address them preemptively")
        
        return suggestions[:3]  # Limit to 3 suggestions for clarity