import asyncio
import time
import unittest
import httpx

CHATBOT_URL = "http://chatbot_api:8000/agent/agent-mongo"

class TestCategorizeByAge(unittest.IsolatedAsyncioTestCase):

    async def make_async_post(self, url, data):
        timeout = httpx.Timeout(timeout=120)
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, timeout=timeout)
            return response


    async def make_bulk_requests(self, url, data):
        tasks = [self.make_async_post(url, payload) for payload in data]
        responses = await asyncio.gather(*tasks)
        outputs = [r.json()["output"] for r in responses]
        return outputs

    questions_stock_hl7fhir = [
        "Qual é o nível de glicose do paciente?",
        "Quais são os valores da pressão arterial do paciente?",
        "Qual é o nome completo do paciente?",
        "Qual é a data de nascimento do paciente?",
        "Qual é o código CID-10 do diagnóstico do paciente?",
        "Qual é a classificação SNOMED CT do diagnóstico do paciente?",
        "Quando o paciente foi admitido em 12/04/2023?",
        "Qual é a data de admissão do paciente em 25/06/2023?",
        "O paciente foi prescrito medicamento A?",
        "Qual é o tratamento prescrito para o paciente?",
        "Qual é o nível de colesterol do paciente?",
        "O hemograma completo do paciente está disponível?",
        "A consulta do paciente está agendada?",
        "A consulta do paciente foi concluída ou cancelada?",
        "Qual é o ID da internação do paciente?",
        "O paciente com ID de internação 12345 já recebeu alta?",
        "Qual é a severidade da condição do paciente?",
        "A condição do paciente é grave ou leve?",
        "Qual é a unidade de medida para o nível de glicose?",
        "A pressão arterial do paciente está em mmHg?",
        "O paciente precisa fazer um raio-X de tórax?",
        "Foi solicitada uma ultrassonografia abdominal para o paciente?",
        "O paciente recebeu a vacina contra COVID-19?",
        "Quando o paciente tomou a vacina contra a gripe?"
    ]

    request_bodies = [{"text": q} for q in questions_stock_financialdocument]

    start_time = time.perf_counter()
    outputs = asyncio.run(make_bulk_requests(CHATBOT_URL, request_bodies))
    end_time = time.perf_counter()

    print(f"Run time: {end_time - start_time} seconds")
