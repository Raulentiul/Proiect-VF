# src/extractor.py
import re

LANG_PATTERNS = [
    (r'\bPython\b', 'Python'),
    (r'\bC\+\+\b', 'C++'),
    (r'\bC\b', 'C'),
    (r'\bJava\b', 'Java'),
    (r'\bLLVM\b', 'LLVM'),
    (r'\bHaskell\b', 'Haskell'),
    (r'\bOCaml\b', 'OCaml'),
    (r'\bMATLAB\b', 'MATLAB'),
]

INPUT_PATTERNS = [
    (r'SMT-LIB', 'SMT-LIB'),
    (r'\bSMT\b', 'SMT'),
    (r'\bQBF\b', 'QBF'),
    (r'\bCNF\b', 'CNF'),
    (r'\bLLVM bitcode\b', 'LLVM bitcode'),
    (r'\bC source\b', 'C source'),
    (r'\bONNX\b', 'ONNX'),
    (r'\bPyTorch\b', 'PyTorch'),
]

PROPERTY_PATTERNS = [
    (r'termination', 'termination'),
    (r'functional correctness', 'functional correctness'),
    (r'complexity bounds', 'complexity bounds'),
    (r'robustness', 'robustness'),
    (r'adversarial', 'adversarial robustness'),
    (r'safety', 'safety'),
    (r'liveness', 'liveness'),
    (r'security', 'security'),
]

EXTERNAL_TOOL_PATTERNS = [
    (r'\bZ3\b', 'Z3'),
    (r'\bCVC4\b', 'CVC4'),
    (r'\bCVC5\b', 'CVC5'),
    (r'\bCBMC\b', 'CBMC'),
    (r'\bBoolector\b', 'Boolector'),
    (r'\bSPIN\b', 'SPIN'),
    (r'\bTensorFlow\b', 'TensorFlow'),
    (r'\bPyTorch\b', 'PyTorch'),
]

def extract_from_text(text):
    text = text or ""
    found = {
        "languages": set(),
        "input_formats": set(),
        "properties": set(),
        "external_tools": set(),
        "techniques": set()
    }
    for pat, label in LANG_PATTERNS:
        if re.search(pat, text, re.I):
            found["languages"].add(label)
    for pat, label in INPUT_PATTERNS:
        if re.search(pat, text, re.I):
            found["input_formats"].add(label)
    for pat, label in PROPERTY_PATTERNS:
        if re.search(pat, text, re.I):
            found["properties"].add(label)
    for pat, label in EXTERNAL_TOOL_PATTERNS:
        if re.search(pat, text, re.I):
            found["external_tools"].add(label)
    # technique heuristics (keywords)
    if re.search(r'\babstract interpretation\b', text, re.I):
        found["techniques"].add("abstract interpretation")
    if re.search(r'\bmodel checking\b', text, re.I):
        found["techniques"].add("model checking")
    if re.search(r'\bSMT\b', text, re.I) or re.search(r'\bSolver\b', text, re.I):
        found["techniques"].add("SMT solving")
    if re.search(r'\bneural network\b|\bneural-network\b|\bNN\b', text, re.I):
        found["techniques"].add("neural network verification techniques")
    return {k:list(v) for k,v in found.items()}
