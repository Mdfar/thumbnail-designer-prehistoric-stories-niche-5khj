import openai

def generate_visual_concept(script_summary): """ Analyzes prehistoric story scripts to generate psychological 'curiosity-gap' thumbnail prompts. """ client = openai.OpenAI()

system_prompt = (
    "You are a YouTube Thumbnail Strategist specializing in the prehistoric niche. "
    "Create high-contrast, cinematic visual concepts that build mystery."
)

user_prompt = f"Based on this script: {script_summary}, suggest 2 thumbnail concepts."

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)
return response.choices[0].message.content