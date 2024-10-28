from transformers import AutoModelForCausalLM, AutoTokenizer


# Model for generating responses using LLaMA 3.2
model_name = "meta-llama/Llama-3.2-3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(**inputs,max_length=150)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response