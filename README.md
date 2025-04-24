# **Projeto: Filtros FIR e IIR em Áudio, Imagens e Vídeos**  

🔊 **Áudio** | 📸 **Imagens** | 🎥 **Vídeos**  

Este repositório contém implementações e estudos sobre filtros digitais **FIR (Finite Impulse Response)** e **IIR (Infinite Impulse Response)** aplicados ao processamento de sinais em áudio, imagens e vídeos.  

---

## **📌 Visão Geral**  
Filtros FIR e IIR são amplamente utilizados em processamento digital de sinais (DSP) para:  
- **Áudio**: Equalização, redução de ruído, efeitos sonoros.  
- **Imagens**: Suavização, detecção de bordas, realce.  
- **Vídeos**: Estabilização, remoção de ruído, compressão.  

Este projeto explora implementações em **Python** e **MATLAB**, com exemplos práticos e comparações entre FIR e IIR.  

---

## **📂 Estrutura do Repositório**  

```bash
├── audio/                  # Processamento de áudio com FIR/IIR  
│   ├── fir_filter.py       # Implementação de filtro FIR para áudio  
│   ├── iir_filter.py       # Implementação de filtro IIR (Butterworth, Chebyshev)  
│   └── examples/           # Exemplos de aplicação (equalização, noise reduction)  
│  
├── images/                 # Filtros em imagens  
│   ├── edge_detection.py   # Filtros FIR (Sobel, Prewitt)  
│   ├── gaussian_blur.py    # Filtro Gaussiano (FIR-like)  
│   └── denoising/          # Redução de ruído (FIR vs IIR)  
│  
├── videos/                 # Processamento de vídeo  
│   ├── temporal_filter.py  # Filtro IIR para estabilização  
│   └── motion_blur.py      # Compensação de movimento com FIR  
│  
├── docs/                   # Teoria, referências e tutoriais  
│   ├── fir_vs_iir.md       # Comparação entre FIR e IIR  
│   └── references.md       # Artigos e livros recomendados  
│  
└── LICENSE                 # Licença (MIT)  
```

---

## **🚀 Como Usar**  

### **Pré-requisitos**  
- Python 3.11+ (com `numpy`, `scipy`, `sympy`, `matplotlib`, `soundfile`, `librosa` )  
- 

### **Exemplo: Aplicando um Filtro FIR em Áudio**  
```python
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Projeto de um filtro FIR passa-baixa
taps = signal.firwin(numtaps=101, cutoff=1000, fs=44100)  

# Aplicando o filtro em um sinal de áudio
audio_signal = np.random.randn(44100)  # Ruído branco como exemplo
filtered_signal = signal.lfilter(taps, 1.0, audio_signal)

# Plotando a resposta em frequência
freq, response = signal.freqz(taps)
plt.plot(freq, 20 * np.log10(abs(response)))
plt.title("Resposta em Frequência do Filtro FIR")
plt.show()
```

---

## **🔍 Comparação FIR vs IIR**  

| **Critério**       | **FIR**                          | **IIR**                          |  
|--------------------|----------------------------------|----------------------------------|  
| **Estabilidade**   | Sempre estável                   | Pode ser instável                |  
| **Eficiência**     | Mais coeficientes                | Menos coeficientes               |  
| **Fase Linear**    | Sim (importante para imagens)    | Não (pode distorcer)             |  
| **Aplicações**     | Áudio (EQ linear), Imagens (bordas) | Áudio (filtros analógicos), Vídeo (temporal) |  

---

## **📚 Referências**  
- **Livros**:  
  - *Digital Signal Processing* — Alan V. Oppenheim  
  - *Digital Image Processing* — Gonzalez & Woods  
- **Artigos**:  
  - [IEEE Xplore: FIR/IIR em Imagens](https://ieeexplore.ieee.org/)  
  - [Google Research: Super-Resolução em Vídeo](https://research.google/)  

---

## **📜 Licença**  
MIT License. Consulte [LICENSE](LICENSE) para detalhes.  

---

## **🤝 Contribuição**  
Contribuições são bem-vindas! Abra uma **issue** ou envie um **pull request**.  

**⭐ Se este projeto te ajudou, deixe uma estrela!**  

--- 

📧 **Contato**: [seu-email@exemplo.com] | [LinkedIn](https://linkedin.com/in/seu-perfil)  

--- 

**🔗 Links Úteis**:  
- [Tutorial FIR em Python](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html)  
- [Exemplos de Filtros IIR](https://www.mathworks.com/help/signal/ref/iirfilter.html)
