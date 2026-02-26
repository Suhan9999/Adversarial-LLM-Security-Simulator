import ollama

def classify_prompt(prompt):

    system_prompt = """
    You are a cybersecurity LLM.

    Classify strictly as:
    malicious
    benign

    Return ONLY valid JSON:

    {
      "classification": "malicious or benign",
      "confidence": float between 0 and 1
    }
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    output = response["message"]["content"]

    try:
        import json
        parsed = json.loads(output)
        classification = parsed["classification"]
        confidence = float(parsed["confidence"])
        confidence = max(0.0, min(confidence, 1.0))

    except Exception:
        # fail safe
        classification = "malicious"
        confidence = 0.0

    return classification, confidence