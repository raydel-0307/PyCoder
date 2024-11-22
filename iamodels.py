from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import time
from metrics import get_time
import torch

def TrainModel(ruta,model_name,settings):

    init_time = time.perf_counter()

    model_path = f"{ruta}/model"

    os.makedirs(model_path, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=settings["torch_dtype"],
        device_map=settings["device_map"],
        cache_dir=model_path
    )
    print(f"Modelo Exportado en {model_path}")

    get_time(init_time)


def MainModel(ruta,model_name,prompt,settings):

    init_time = time.perf_counter()

    model_path = f"{ruta}/model"

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=settings["torch_dtype"],
        device_map=settings["device_map"],
        cache_dir=model_path
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    messages = [
        {"role": "system", "content": "Tu eres ByCoder, creado por  DazLab. Eres un magnifico asistente para la Generacion y Automatizacion de codigos."},
        {"role": "user", "content": prompt}
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=settings["tokenize"],
        add_generation_prompt=settings["add_generation_prompt"]
    )

    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=settings["max_new_tokens"]
    )

    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=settings["skip_special_tokens"])[0]
    print(response)

    get_time(init_time)

    return response