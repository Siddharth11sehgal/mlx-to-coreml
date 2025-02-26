import coremltools as ct
import mlx.core as mx
from mlx_lm import load
import os
import json

def convert_to_mlmodel():
    print("Loading MLX model")
    model, tokenizer = load("your-model-name")

    # Create output directory
    os.makedirs("MLXModel", exist_ok=True)

    # Save model weights
    model.save_weights("MLXModel/model.safetensors")

    # Save tokenizer config
    tokenizer_config = {
        "model_max_length": 2048,
        "pad_token": "<|endoftext|>",
        "bos_token": "<|endoftext|>",
        "eos_token": "<|endoftext|>",
        "unk_token": "<|endoftext|>",
        "tokenizer_class": "GPT2Tokenizer"
    }

    with open("MLXModel/tokenizer.json", "w") as f:
        json.dump(tokenizer_config, f, indent=2)

    # Convert to Core ML
    print("Converting to Core ML...")
    mlmodel = ct.convert(model)

    # Save the .mlmodel file
    mlmodel.save("MLXModel/model.mlmodel")
    print("Model successfully converted to Core ML format!")

    print("\nStep 3: Instructions")
    print("""
    Add these files to your Xcode project:
    1. Add MLXModel folder to your project
    2. Update Info.plist MLXBundleResources:
        <key>MLXBundleResources</key>
        <array>
            <string>model.mlmodel</string>
            <string>tokenizer.json</string>
        </array>
    """)

if __name__ == "__main__":
    convert_to_mlmodel()
