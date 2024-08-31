# Implementação de AES-CTR e RSA com Assinatura Digital - CIC0201 Segurança Computacional 2024/1

## Descrição do Projeto

Este repositório contém a implementação do trabalho de segurança computacional, disciplina do meu 6º semestre de Ciência da Computação na Universidade de Brasília, dividido em duas partes principais:

### **Parte I - Cifra de Bloco e Modo de Operação CTR**

1. **Etapa I:** Implementação da cifra de bloco AES com bloco de 128 bits e chave de 128 bits. A implementação permite especificar o número de rodadas de cifração/decifração.
   
2. **Etapa II:** Implementação do modo de operação CTR (Counter Mode) utilizando a cifra AES implementada anteriormente.

3. **Extra 1:** Implementação do modo de cifração autenticada GCM (Galois/Counter Mode) para AES.

4. **Testes:** Cifração e decifração de um arquivo para validação da implementação.

5. **Extra 2:** Cifração de uma selfie no modo CTR com diferentes números de rodadas do AES (1, 5, 9, e 13 rodadas). Resultados renderizados e anexados ao relatório.

### **Parte II - Gerador/Verificador de Assinaturas RSA**

1. **Etapa I:** Implementação da geração de chaves RSA (com primos de no mínimo 1024 bits) e cifração/decifração assimétrica RSA.

2. **Etapa II:** Implementação da assinatura digital:
   - Cálculo de hashes (SHA-3)
   - Assinatura da mensagem
   - Formatação em BASE64

3. **Etapa III:** Implementação da verificação da assinatura:
   - Parsing do documento assinado
   - Decifração da assinatura e verificação do hash

## Instruções de Uso

Este repositório possui os scripts separados para as diferentes etapas de forma modular. Aqui se encontram scripts de testes e implementação para ambos os algoritmos, assim como, os arquivos usados nos testes, o relatório desenvolvido e a especificação do trabalho.

Para os scripts funcionarem corretamente, é necessário instalar as seguintes bibliotecas:
```
pip install hashlib
pip install PIL
```

Caso deseja rodar todos os testes novamente, é recomendado que mantenha somente os arquivos vitais para gerar o restante dos outros arquivos de saída. Segue a lista dos arquivos vitais para o funcionamento:

- `/AES/arquivos/selfie.jpg`
- `/AES/arquivos/texto.txt`
- `/AES/arquivos/texto_cifrado_openssl.bin`
- `/AES/arquivos/selfie_cifrado_openssl.bin`
- `/RSA/arquivos/selfie.jpg`
- `/RSA/arquivos/texto.txt`
- `/RSA/arquivos/doc.pdf`
