import re
import random
from typing import Dict, List

class DebateMentor:
    def __init__(self):
        """Initialize the Debate Mentor with rule-based logic only."""
        
        # Define logical fallacies patterns
        self.fallacy_patterns = {
            "ad_hominem": {
                "patterns": [
                    r"you are (stupid|dumb|ignorant|wrong|foolish|idiotic)",
                    r"people like you",
                    r"typical (liberal|conservative|democrat|republican)",
                    r"you don't understand",
                    r"you're just",
                    r"you obviously",
                    r"anyone with half a brain"
                ],
                "explanation": "Attacking the person rather than their argument"
            },
            "strawman": {
                "patterns": [
                    r"so you're saying",
                    r"what you really mean",
                    r"you want to",
                    r"your position is that",
                    r"you're claiming that",
                    r"you believe that"
                ],
                "explanation": "Misrepresenting opponent's argument to make it easier to attack"
            },
            "false_dichotomy": {
                "patterns": [
                    r"either.*or",
                    r"only two (options|choices|ways)",
                    r"you must choose",
                    r"there are only",
                    r"it's either.*or nothing"
                ],
                "explanation": "Presenting only two options when more exist"
            },
            "appeal_to_emotion": {
                "patterns": [
                    r"think of the children",
                    r"how can you live with yourself",
                    r"this is heartbreaking",
                    r"imagine if",
                    r"this is disgusting",
                    r"this is outrageous"
                ],
                "explanation": "Using emotional manipulation instead of logical reasoning"
            },
            "hasty_generalization": {
                "patterns": [
                    r"all .* are",
                    r"every .* is",
                    r"always",
                    r"never",
                    r"everybody knows",
                    r"everyone agrees"
                ],
                "explanation": "Making broad conclusions from limited examples"
            },
            "slippery_slope": {
                "patterns": [
                    r"if we allow.*then",
                    r"this will lead to",
                    r"next thing you know",
                    r"where does it end",
                    r"before you know it",
                    r"it's a slippery slope"
                ],
                "explanation": "Assuming one event will lead to extreme consequences"
            },
            "appeal_to_authority": {
                "patterns": [
                    r"experts say",
                    r"studies show",
                    r"scientists agree",
                    r"everyone knows",
                    r"it's common knowledge"
                ],
                "explanation": "Citing authority without proper evidence or context"
            }
        }
        
        # Enhanced argument templates with more variety
        self.argument_templates = {
            "For": [
                "Supporting {topic} is essential because it promotes {benefit} and addresses the critical issue of {problem}.",
                "The evidence clearly demonstrates that {topic} leads to {positive_outcome} and significantly improves {area}.",
                "From an ethical standpoint, {topic} is necessary to ensure {moral_good} and prevent {harm}.",
                "Research consistently shows that {topic} results in measurable improvements in {field}.",
                "The practical benefits of {topic} include {benefit} and the reduction of {problem}.",
                "Historical precedent supports {topic} as it has proven effective in {context}.",
                "Economic analysis reveals that {topic} generates {positive_outcome} while minimizing {concern}."
            ],
            "Against": [
                "Opposing {topic} is crucial because it prevents {negative_outcome} and protects our fundamental {value}.",
                "The risks associated with {topic} far outweigh any potential benefits, particularly regarding {concern}.",
                "Historical evidence shows that {topic} has consistently led to {negative_consequence} in {context}.",
                "From a practical perspective, {topic} is unfeasible due to {obstacle} and significant {limitation}.",
                "The unintended consequences of {topic} include {harm} and the erosion of {value}.",
                "Economic analysis reveals that {topic} would result in {negative_outcome} and increased {concern}.",
                "Ethical considerations demand we reject {topic} to preserve {moral_good} and prevent {harm}."
            ]
        }
        
        # Enhanced template fillers with more variety
        self.template_fillers = {
            "benefit": ["social equality", "technological innovation", "economic prosperity", "educational advancement", "healthcare improvements", "environmental protection", "individual freedom", "community safety"],
            "problem": ["systemic inequality", "economic inefficiency", "social injustice", "environmental degradation", "public health risks", "educational gaps", "technological disparity"],
            "positive_outcome": ["increased prosperity", "improved health outcomes", "enhanced security", "greater equality", "technological advancement", "environmental sustainability", "social cohesion"],
            "negative_outcome": ["economic instability", "loss of privacy", "increased inequality", "social division", "environmental damage", "public safety risks", "erosion of rights"],
            "area": ["public education", "healthcare systems", "economic development", "social welfare", "environmental policy", "technological infrastructure", "community relations"],
            "moral_good": ["justice", "fairness", "human dignity", "equality", "freedom", "compassion", "integrity", "respect for rights"],
            "harm": ["discrimination", "exploitation", "suffering", "injustice", "oppression", "environmental damage", "economic hardship", "social fragmentation"],
            "value": ["individual liberty", "democratic principles", "economic stability", "social cohesion", "cultural diversity", "personal privacy", "community values"],
            "concern": ["privacy violations", "economic disruption", "unintended consequences", "abuse of power", "social inequality", "environmental impact", "public safety"],
            "field": ["public health metrics", "economic indicators", "educational outcomes", "environmental measures", "social welfare statistics", "technological adoption rates"],
            "context": ["similar circumstances", "comparable situations", "historical precedents", "international examples", "previous implementations"],
            "obstacle": ["implementation challenges", "resource limitations", "political opposition", "technical difficulties", "regulatory barriers"],
            "limitation": ["budget constraints", "technological barriers", "social resistance", "legal restrictions", "practical challenges"],
            "negative_consequence": ["economic decline", "social unrest", "increased inequality", "environmental damage", "loss of freedoms", "public dissatisfaction"]
        }

        # Counter-argument strategies
        self.counter_strategies = [
            "However, this perspective overlooks the significant {concern} that could arise from {topic}.",
            "While your argument has merit, it fails to address the potential {negative_outcome} and {limitation}.",
            "This viewpoint doesn't fully consider the {obstacle} that would make {topic} impractical.",
            "Although you raise valid points, the evidence suggests that {topic} often leads to {negative_consequence}.",
            "Your argument assumes ideal conditions, but real-world implementation would face {limitation} and {concern}.",
            "While theoretically sound, this position ignores the {harm} that vulnerable populations might experience.",
            "This perspective may be too optimistic about {topic}, given the historical tendency toward {negative_consequence}."
        ]

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
            context=random.choice(self.template_fillers["context"]),
            obstacle=random.choice(self.template_fillers["obstacle"]),
            limitation=random.choice(self.template_fillers["limitation"]),
            negative_consequence=random.choice(self.template_fillers["negative_consequence"])
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
        
        # Add specific rebuttals based on argument content
        rebuttals = []
        argument_lower = user_argument.lower()
        
        if any(word in argument_lower for word in ["benefit", "advantage", "positive", "good"]):
            strategy = random.choice(self.counter_strategies)
            rebuttal = strategy.format(
                topic=topic.lower(),
                concern=random.choice(self.template_fillers["concern"]),
                negative_outcome=random.choice(self.template_fillers["negative_outcome"]),
                limitation=random.choice(self.template_fillers["limitation"]),
                obstacle=random.choice(self.template_fillers["obstacle"]),
                negative_consequence=random.choice(self.template_fillers["negative_consequence"]),
                harm=random.choice(self.template_fillers["harm"])
            )
            rebuttals.append(rebuttal)
        
        if any(word in argument_lower for word in ["research", "study", "evidence", "data"]):
            rebuttals.append("While some studies support this view, conflicting research and methodological concerns suggest the evidence is not as conclusive as presented.")
        
        if any(word in argument_lower for word in ["moral", "ethical", "right", "wrong"]):
            rebuttals.append("This raises important questions about competing ethical frameworks and whose moral standards should take precedence in a diverse society.")
        
        if any(word in argument_lower for word in ["freedom", "rights", "liberty"]):
            rebuttals.append("We must carefully balance individual freedoms with collective responsibilities and consider how these rights impact other members of society.")
        
        # Combine base argument with specific rebuttals
        if rebuttals:
            return f"{base_counter} {random.choice(rebuttals)}"
        else:
            return f"{base_counter} Additionally, your argument doesn't fully address the potential negative implications and alternative perspectives that need consideration."

    def get_improvement_suggestions(self, argument: str, fallacy_analysis: Dict) -> List[str]:
        """Provide suggestions for improving the argument."""
        suggestions = []
        argument_lower = argument.lower()
        
        # Fallacy-specific suggestions
        if fallacy_analysis["has_fallacies"]:
            suggestions.append("Address the logical fallacies identified to strengthen your reasoning")
            suggestions.append("Focus on evidence-based claims rather than emotional appeals or personal attacks")
        
        # Length and depth analysis
        word_count = len(argument.split())
        if word_count < 30:
            suggestions.append("Expand your argument with more detailed reasoning and specific examples")
        elif word_count < 50:
            suggestions.append("Consider adding more supporting evidence or addressing potential counterarguments")
        
        # Structure analysis
        if not any(word in argument_lower for word in ["because", "since", "therefore", "thus", "as a result"]):
            suggestions.append("Add clear causal reasoning using connecting words like 'because', 'since', or 'therefore'")
        
        # Evidence analysis
        if not any(word in argument_lower for word in ["research", "study", "evidence", "data", "statistics", "survey"]):
            suggestions.append("Include references to research, data, or credible sources to support your claims")
        
        # Balance analysis
        if not any(word in argument_lower for word in ["however", "although", "while", "despite", "nevertheless"]):
            suggestions.append("Acknowledge potential counterarguments or limitations to demonstrate balanced thinking")
        
        # Tone analysis
        exclamation_count = argument.count("!")
        if exclamation_count > 2:
            suggestions.append("Adopt a more measured tone - excessive emphasis can weaken your argument's credibility")
        
        # Specificity analysis
        if not any(word in argument_lower for word in ["example", "instance", "case", "specifically", "particularly"]):
            suggestions.append("Include specific examples or case studies to make your argument more concrete and persuasive")
        
        # Ensure we always have suggestions
        if not suggestions:
            suggestions.extend([
                "Consider strengthening your argument with more detailed explanations",
                "Think about potential objections and address them preemptively",
                "Add more specific examples to illustrate your main points"
            ])
        
        return suggestions[:4]  # Limit to 4 suggestions for clarity

    def analyze_argument_strength(self, argument: str) -> Dict[str, int]:
        """Analyze various aspects of argument strength."""
        word_count = len(argument.split())
        sentence_count = len([s for s in re.split(r'[.!?]+', argument) if s.strip()])
        
        # Count evidence indicators
        evidence_words = ['research', 'study', 'data', 'statistics', 'evidence', 'survey', 'report']
        evidence_count = sum(1 for word in evidence_words if word in argument.lower())
        
        # Count reasoning indicators
        reasoning_words = ['because', 'since', 'therefore', 'thus', 'consequently', 'as a result', 'hence']
        reasoning_count = sum(1 for word in reasoning_words if word in argument.lower())
        
        # Count balance indicators
        balance_words = ['however', 'although', 'while', 'despite', 'nevertheless', 'but', 'yet']
        balance_count = sum(1 for word in balance_words if word in argument.lower())
        
        return {
            'word_count': word_count,
            'sentence_count': sentence_count,
            'evidence_indicators': evidence_count,
            'reasoning_indicators': reasoning_count,
            'balance_indicators': balance_count
        }