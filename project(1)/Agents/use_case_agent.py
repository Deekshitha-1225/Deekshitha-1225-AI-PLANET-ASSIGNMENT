def generate_use_cases(industry_info):
    use_cases = []
    if "Healthcare" in industry_info:
        use_cases.append("AI-powered diagnostics assistant for healthcare.")
        use_cases.append("Patient data analytics for predictive health outcomes.")
    elif "Retail" in industry_info:
        use_cases.append("Personalized shopping recommendations.")
        use_cases.append("AI chatbots for customer support.")

    return use_cases

# Example
if __name__ == "__main__":
    industry_info = ["Healthcare", "Diagnostics", "AI Adoption"]
    cases = generate_use_cases(industry_info)
    print(cases)
