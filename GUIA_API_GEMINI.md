# 🚨 Guia Definitivo: Resolução de Problemas com a API do Google Gemini (Atualização 2026)

Este documento foi criado para registrar a solução de uma série de problemas complexos de integração com a API do Google Generative Language (Gemini), especialmente ao usar requisições `fetch` diretas no frontend (HTML/JS) com contas mais recentes do Google AI Studio / Google Cloud.

Se você está recebendo erros como `Expected OAuth 2 access token` ou `models/gemini-1.5-flash is not found`, este é o manual definitivo para resolver.

---

## 1. O Problema das Chaves "AQ." (Erro de OAuth 2)

**Sintoma:** Você tenta usar a sua chave de API e recebe o erro:
> *"Request had invalid authentication credentials. Expected OAuth 2 access token..."*

**O que mudou (Contexto):**
Historicamente, o Google gerava chaves no formato **`AIzaSy`**. Recentemente, novos projetos passaram a gerar chaves de autenticação no formato **`AQ.*`**. 
Muitas IAs e tutoriais antigos orientam a colocar chaves `AQ.` dentro de um cabeçalho HTTP `Authorization: Bearer`. **Isso está errado para uso simples no frontend.**

**A Solução:**
- A chave `AQ.` é perfeitamente válida.
- Ela **NÃO** deve ser enviada via cabeçalho `Authorization`. 
- Ela deve ser passada **EXCLUSIVAMENTE via parâmetro de URL (`?key=SuaChaveAQ`)**.

**Como deve ficar o seu código:**
```javascript
// CORRETO
const fetchUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=AQ.SuaChaveAqui`;

const response = await fetch(fetchUrl, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' }, // Sem cabeçalho Authorization!
    body: JSON.stringify({...})
});
```

---

## 2. O Problema de Modelos Aposentados (Erro 404 / Not Found)

**Sintoma:** A sua chave passa pela segurança, mas você recebe um erro semelhante a:
> *"models/gemini-1.5-flash is not found for API version v1beta"* ou
> *"This model is no longer available to new users. Please update your code to use models/gemini-3.8-flash"*

**O que mudou (Contexto):**
O Google atualiza seus modelos de forma agressiva. Modelos como `gemini-pro` antigo ou `gemini-1.5-flash` podem ser desligados para novos usuários, gerando um erro literal de "não encontrado". O seu IDE ou assistente de IA pode não saber disso por estar com o contexto desatualizado.

**A Solução:**
- Atualize sempre a string da URL para a versão mais recente exigida pelo servidor (ex: substituir `gemini-1.5-flash` por **`gemini-3.8-flash`**).

---

## 3. Prompt de Resgate (Copie e Cole para IAs)

Quando você estiver em um novo projeto, e o ChatGPT, Claude, ou Antigravity começar a se enrolar sugerindo OAuth 2.0 ou reclamando que a chave `AQ.` é inválida, **copie e cole o prompt abaixo para forçar a IA a entender o contexto atualizado:**

<details>
<summary><b>Clique para copiar o Prompt de Resgate</b></summary>

```text
🚨 PARE! ATUALIZAÇÃO CRÍTICA DE CONTEXTO DA API DO GOOGLE GEMINI (2026) 🚨

Estou desenvolvendo uma integração direta no frontend (HTML/JS) usando fetch para a API generativelanguage.googleapis.com. Por favor, ajuste suas respostas baseadas nas seguintes regras absolutas da arquitetura mais recente:

1. CHAVES AQ: A minha chave começa com "AQ.". Esta é a chave de autenticação correta. Você NÃO deve me mandar configurar tokens OAuth 2.0 ou Service Accounts.
2. CABEÇALHOS: Você NÃO deve colocar a minha chave "AQ." em um cabeçalho `Authorization: Bearer`. Se você fizer isso, o Google vai rejeitar com erro de OAuth.
3. ENVIO: A chave "AQ." deve ser enviada EXCLUSIVAMENTE via parâmetro de URL (`?key=AQ...`). O único header permitido no fetch é `Content-Type: application/json`.
4. VERSÃO DO MODELO: O Google desligou modelos antigos (como gemini-1.5-flash) para novos projetos, gerando erro "not found". A URL base do meu fetch deve OBRIGATORIAMENTE bater no endpoint mais novo exigido (ex: `models/gemini-3.8-flash:generateContent`).

Por favor, refaça o meu código ou análise levando em consideração todas essas 4 regras.
```
</details>

---
*Documentado após batalha épica em 26 de Setembro de 2026.*
