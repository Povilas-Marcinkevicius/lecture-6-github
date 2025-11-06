# 🖼️ Paveikslėlio Aprašymas su AI

Streamlit programa, kuri naudoja Ollama vision modelį paveikslėlių turiniui apibūdinti.

## Aprašymas

Ši programa leidžia vartotojui įkelti paveikslėlį per naršyklę, o dirbtinis intelektas (Ollama modelis) apibūdina paveikslėlio turinį lietuvių kalba.

## Reikalavimai

- Python 3.8 arba naujesnė versija
- Ollama serveris (paleistas lokaliame kompiuteryje)
- Ollama modelis gemma3:4b

## Instaliacija

1. Klonuokite repozitoriją:
```bash
git clone https://github.com/Povilas-Marcinkevicius/lecture-6-github.git
cd lecture-6-github
```

2. Įdiekite reikalingas priklausomybes:
```bash
pip install -r requirements.txt
```

3. Įsitikinkite, kad Ollama serveris veikia ir modelis parsisiųstas:
```bash
# Paleiskite Ollama serverį (jei dar nepaleistas)
ollama serve

# Parsisiųskite gemma3:4b modelį
ollama pull gemma3:4b
```

## Paleidimas

Paleiskite Streamlit programą:
```bash
streamlit run app.py
```

Naršyklė turėtų automatiškai atidaryti programą adresu `http://localhost:8501`

## Naudojimas

1. Atidarykite programą naršyklėje
2. Įkelkite paveikslėlį (JPG, PNG, BMP arba GIF formatu)
3. Paspauskite mygtuką "Analizuoti paveikslėlį"
4. Palaukite kol AI apibūdins paveikslėlio turinį

## Technologijos

- **Streamlit** - Web sąsaja
- **Ollama** - Dirbtinio intelekto modeliai
- **Pillow** - Paveikslėlių apdorojimas
- **gemma3:4b** - Multimodalus modelis paveikslėlių analizei
