# MLX to Core ML Converter  

**Convert MLX-based Large Language Models (LLMs) to Apple's Core ML (.mlmodel) format for seamless integration into macOS and iOS applications.**  

## Overview  

Machine learning models trained using MLX can be converted to Core ML for use in Apple applications. This tool automates the conversion process, ensuring that your model is optimized and ready for Xcode integration.  

### Features  
✔️ Converts MLX models to `.mlmodel` format  
✔️ Saves tokenizer configurations for easy use  
✔️ Generates a structured `MLXModel/` folder for easy integration  
✔️ Simple one-command execution  

---

##  Installation  

Before running the conversion script, install the required dependencies.  

### **Option 1: Install Manually**  
Run the following command:  

```bash
pip install coremltools mlx mlx-lm
```

### **Option 2: Install via `requirements.txt`**  
For an easier setup, use:  

```bash
pip install -r requirements.txt
```

> **Note:** Ensure you have Python 3.8+ installed. You can check your version using:  

```bash
python --version
```

---

## Usage  

### **1. Clone the Repository**  

```bash
git clone https://github.com/your-username/mlx-to-coreml.git
cd mlx-to-coreml
```

### **2. Run the Conversion Script**  

To convert an MLX model, simply run:  

```bash
python convert.py
```

### **3. Expected Output**  

Once completed, the converted Core ML model will be saved in the `MLXModel/` directory:

```
📂 MLXModel/
 ├── model.mlmodel      # Converted Core ML model
 ├── model.safetensors  # MLX model weights
 ├── tokenizer.json     # Tokenizer configuration
```

---

## Adding the Model to Xcode  

Once the `.mlmodel` file is generated, follow these steps to integrate it into an Xcode project:

### **1. Drag and Drop**
- Open Xcode and **drag the entire `MLXModel/` folder** into your project.

### **2. Update `Info.plist`**
Add the following under `MLXBundleResources` in `Info.plist`:

```xml
<key>MLXBundleResources</key>
<array>
    <string>model.mlmodel</string>
    <string>tokenizer.json</string>
</array>
```

### **3. Use the Model in Your Swift Code**
You can now use Core ML in Swift:

```swift
import CoreML

let model = try MLModel(contentsOf: Bundle.main.url(forResource: "model", withExtension: "mlmodelc")!)
```


This is now a **fully detailed README** with clear installation instructions, dependencies, troubleshooting, and a professional structure. Let me know if you want any changes! 🚀
