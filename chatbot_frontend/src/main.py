import os
import requests
import streamlit as st

CHATBOT_URL = os.getenv('CHATBOT_URL', "http://chatbot_api:8000/agent/agent-mongo")

with st.sidebar:
    st.header("Sobre")
    st.markdown(
        """
        Este chatbot interage com alguns recursos listados aqui
        [HL7 Resource](https://www.hl7.org/fhir/resourcelist.html)
        agente projetado para responder perguntas sobre alguns recursos do HL7.
        O agente usa geração aumentada por recuperação (RAG) sobre dados
        estruturados e não estruturados que foram gerados sinteticamente.
        """
    )

    st.header("Perguntas de Exemplo")

    st.subheader("OBSERVATION")
    st.markdown("- Qual é o nível de glicose do paciente?")
    st.markdown("- Quais são os valores da pressão arterial do paciente?")

    st.subheader("PATIENT")
    st.markdown("- Qual é o nome completo do paciente?")
    st.markdown("- Qual é a data de nascimento do paciente?")

    st.subheader("DIAGNOSIS")
    st.markdown("- Qual é o código CID-10 do diagnóstico do paciente?")
    st.markdown("- Qual é a classificação SNOMED CT do diagnóstico do paciente?")

    st.subheader("ADMISSIONDATE")
    st.markdown("- Quando o paciente foi admitido em 12/04/2023?")
    st.markdown("- Qual é a data de admissão do paciente em 25/06/2023?")

    st.subheader("PRESCRIPTION")
    st.markdown("- O paciente foi prescrito medicamento A?")
    st.markdown("- Qual é o tratamento prescrito para o paciente?")

    st.subheader("LABRESULT")
    st.markdown("- Qual é o nível de colesterol do paciente?")
    st.markdown("- O hemograma completo do paciente está disponível?")

    st.subheader("APPOINTMENTSTATUS")
    st.markdown("- A consulta do paciente está agendada?")
    st.markdown("- A consulta do paciente foi concluída ou cancelada?")

    st.subheader("ENCOUNTERID")
    st.markdown("- Qual é o ID da internação do paciente?")
    st.markdown("- O paciente com ID de internação 12345 já recebeu alta?")

    st.subheader("SEVERITY")
    st.markdown("- Qual é a severidade da condição do paciente?")
    st.markdown("- A condição do paciente é grave ou leve?")

    st.subheader("UNITOFMEASURE")
    st.markdown("- Qual é a unidade de medida para o nível de glicose?")
    st.markdown("- A pressão arterial do paciente está em mmHg?")

    st.subheader("PROCEDUREREQUEST")
    st.markdown("- O paciente precisa fazer um raio-X de tórax?")
    st.markdown("- Foi solicitada uma ultrassonografia abdominal para o paciente?")

    st.subheader("IMMUNIZATION")
    st.markdown("- O paciente recebeu a vacina contra COVID-19?")
    st.markdown("- Quando o paciente tomou a vacina contra a gripe?")


st.title("<<-- _SMART FHIR_ -->>")
st.title('[Chatbot Especialista em recursos do HL7 FHIR]')
st.info(
    """Pergunte-me sobre os recursos de um paciente, diagnósticos, observações médicas,
    e mais informações relacionadas ao recursos HL7 FHIR."""
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "output" in message.keys():
            st.markdown(message["output"])

        if "explanation" in message.keys():
            with st.status("Como isso foi gerado?", state="complete"):
                st.info(message["explanation"])

if prompt := st.chat_input("O que você quer saber?"):
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({"role": "user", "output": prompt})

    data = {"text": prompt, "session_id": "abc"}

    with st.spinner("Procurando por uma resposta..."):
        response = requests.post(CHATBOT_URL, json=data)

        if response.status_code == 200:
            output_text = response.json().get("output", "Nenhuma resposta disponível.")
            explanation = response.json().get("intermediate_steps", "Nenhuma explicação disponível.")
        else:
            output_text = """Ocorreu um erro ao processar sua mensagem.
            Por favor, tente novamente ou reformule sua mensagem."""
            explanation = output_text

    st.chat_message("assistant").markdown(output_text)
    st.status("Como isso foi gerado?", state="complete").info(explanation)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "output": output_text,
            "explanation": explanation,
        }
    )