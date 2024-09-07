from langchain.schema import Document

docs = [
    Document(
        page_content="Representa uma instância de um recurso de observação médica, geralmente utilizada para representar dados sobre um paciente.",
        metadata={
            "key": "OBSERVATION",
            "values": [
                "nível de glicose",
                "frequência cardíaca",
                "pressão arterial"
            ],
            "example_answer": [
                {"OBSERVATION": "nível de glicose"}
            ]
        }
    ),
    Document(
        page_content="Conjunto de informações de um paciente, como nome, data de nascimento e histórico médico.",
        metadata={
            "key": "PATIENT",
            "values": [
                "nome completo",
                "data de nascimento",
                "sexo",
                "endereço"
            ],
            "example_answer": [
                {"PATIENT": "nome completo"}
            ]
        }
    ),
    Document(
        page_content="Código de identificação que define o diagnóstico de um paciente com base em sistemas padronizados, como o CID-10.",
        metadata={
            "key": "DIAGNOSIS",
            "values": [
                "CID-10",
                "CID-11",
                "SNOMED CT"
            ],
            "example_answer": [
                {"DIAGNOSIS": "CID-10"}
            ]
        }
    ),
    Document(
        page_content="Momento em que o paciente foi admitido no hospital ou outra instituição de saúde.",
        metadata={
            "key": "ADMISSIONDATE",
            "values": [
                "12/04/2023",
                "01/03/2023",
                "25/06/2023"
            ],
            "example_answer": [
                {"ADMISSIONDATE": "12/04/2023"}
            ]
        }
    ),
    Document(
        page_content="Documento que formaliza uma receita médica, contendo orientações sobre medicamentos ou tratamentos prescritos ao paciente.",
        metadata={
            "key": "PRESCRIPTION",
            "values": [
                "medicamento A",
                "medicamento B",
                "tratamento X"
            ],
            "example_answer": [
                {"PRESCRIPTION": "medicamento A"}
            ]
        }
    ),
    Document(
        page_content="Resultado de testes laboratoriais realizados em amostras de um paciente.",
        metadata={
            "key": "LABRESULT",
            "values": [
                "nível de colesterol",
                "hemograma completo"
            ],
            "example_answer": [
                {"LABRESULT": "nível de colesterol"}
            ]
        }
    ),
    Document(
        page_content="Indica o status atual da consulta de um paciente, como agendada, concluída ou cancelada.",
        metadata={
            "key": "APPOINTMENTSTATUS",
            "values": [
                "agendada",
                "concluída",
                "cancelada"
            ],
            "example_answer": [
                {"APPOINTMENTSTATUS": "agendada"}
            ]
        }
    ),
    Document(
        page_content="Número de identificação único atribuído a uma internação de paciente em um hospital ou instituição de saúde.",
        metadata={
            "key": "ENCOUNTERID",
            "values": [
                "12345",
                "67890",
                "11223"
            ],
            "example_answer": [
                {"ENCOUNTERID": "12345"}
            ]
        }
    ),
    Document(
        page_content="Classificação da severidade da condição ou doença do paciente.",
        metadata={
            "key": "SEVERITY",
            "values": [
                "leve",
                "moderada",
                "grave"
            ],
            "example_answer": [
                {"SEVERITY": "grave"}
            ]
        }
    ),
    Document(
        page_content="Unidade de medida utilizada para quantificar a dose de medicamento ou resultados de exames.",
        metadata={
            "key": "UNITOFMEASURE",
            "values": [
                "mg/dL",
                "mmHg",
                "bpm"
            ],
            "example_answer": [
                {"UNITOFMEASURE": "mg/dL"}
            ]
        }
    ),
    Document(
        page_content="Representa a solicitação para a realização de um procedimento médico ou terapêutico.",
        metadata={
            "key": "PROCEDUREREQUEST",
            "values": [
                "raio-X de tórax",
                "ultrassonografia abdominal",
                "ressonância magnética"
            ],
            "example_answer": [
                {"PROCEDUREREQUEST": "raio-X de tórax"}
            ]
        }
    ),
    Document(
        page_content="Detalha a imunização administrada ao paciente, incluindo a data e tipo de vacina.",
        metadata={
            "key": "IMMUNIZATION",
            "values": [
                "vacina contra a gripe",
                "vacina contra o sarampo",
                "vacina COVID-19"
            ],
            "example_answer": [
                {"IMMUNIZATION": "vacina COVID-19"}
            ]
        }
    ),
    Document(
        page_content="Indica o plano de tratamento ou cuidados contínuos recomendados para o paciente.",
        metadata={
            "key": "CAREPLAN",
            "values": [
                "fisioterapia",
                "tratamento medicamentoso",
                "monitoramento contínuo"
            ],
            "example_answer": [
                {"CAREPLAN": "fisioterapia"}
            ]
        }
    ),
    Document(
        page_content="Conjunto de informações relacionadas à alta hospitalar, incluindo orientações e medicamentos prescritos para o paciente.",
        metadata={
            "key": "DISCHARGESUMMARY",
            "values": [
                "orientações pós-operatórias",
                "prescrição de medicamentos",
                "marcação de consulta de retorno"
            ],
            "example_answer": [
                {"DISCHARGESUMMARY": "orientações pós-operatórias"}
            ]
        }
    ),
    Document(
        page_content="Indica as instruções para a administração de medicamentos, incluindo dosagem e frequência.",
        metadata={
            "key": "MEDICATIONREQUEST",
            "values": [
                "tomar 1 comprimido 2 vezes ao dia",
                "aplicar pomada 3 vezes ao dia",
                "injeção intramuscular a cada 6 horas"
            ],
            "example_answer": [
                {"MEDICATIONREQUEST": "tomar 1 comprimido 2 vezes ao dia"}
            ]
        }
    ),
    Document(
        page_content="Detalha o histórico de alergias do paciente, como a reação a medicamentos ou alimentos.",
        metadata={
            "key": "ALLERGYINTOLERANCE",
            "values": [
                "alergia a penicilina",
                "intolerância a lactose",
                "reação adversa a frutos do mar"
            ],
            "example_answer": [
                {"ALLERGYINTOLERANCE": "alergia a penicilina"}
            ]
        }
    ),
    Document(
        page_content="Indica o status da entrega de medicamentos prescritos ao paciente.",
        metadata={
            "key": "DISPENSESTATUS",
            "values": [
                "dispensado",
                "pendente",
                "não dispensado"
            ],
            "example_answer": [
                {"DISPENSESTATUS": "dispensado"}
            ]
        }
    ),
    Document(
        page_content="A descrição do grupo ou subgrupo etário ao qual o paciente pertence.",
        metadata={
            "key": "AGEGROUP",
            "values": [
                "criança",
                "adulto",
                "idoso"
            ],
            "example_answer": [
                {"AGEGROUP": "adulto"}
            ]
        }
    ),
    Document(
        page_content="Representa as informações sobre a localização onde o cuidado está sendo prestado ao paciente.",
        metadata={
            "key": "LOCATION",
            "values": [
                "UTI",
                "enfermaria",
                "sala de emergência"
            ],
            "example_answer": [
                {"LOCATION": "UTI"}
            ]
        }
    ),
    Document(
        page_content="Informações sobre o estado civil do paciente, importantes para documentar aspectos legais e sociais.",
        metadata={
            "key": "MARITALSTATUS",
            "values": [
                "solteiro",
                "casado",
                "divorciado"
            ],
            "example_answer": [
                {"MARITALSTATUS": "casado"}
            ]
        }
    ),
    Document(
        page_content="Informações sobre os contatos de emergência, listando parentes ou cuidadores primários.",
        metadata={
            "key": "EMERGENCYCONTACT",
            "values": [
                "mãe",
                "pai",
                "cônjuge"
            ],
            "example_answer": [
                {"EMERGENCYCONTACT": "mãe"}
            ]
        }
    ),
    Document(
        page_content="A descrição dos sinais vitais do paciente no momento do atendimento.",
        metadata={
            "key": "VITALSIGNS",
            "values": [
                "pressão arterial",
                "frequência cardíaca",
                "temperatura corporal"
            ],
            "example_answer": [
                {"VITALSIGNS": "pressão arterial"}
            ]
        }
    )
]