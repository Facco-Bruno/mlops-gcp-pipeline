# MLOps Pipeline on GCP

Este repositório contém uma solução completa para criar um pipeline de MLOps na Google Cloud Platform (GCP). O projeto inclui a criação de infraestrutura, treinamento de modelos de machine learning, implantação automatizada e monitoramento.

## Sumário

1. [Pré-requisitos](#pré-requisitos)
2. [Passo 1: Configuração Inicial](#passo-1-configuração-inicial)
3. [Passo 2: Provisionamento da Infraestrutura com Terraform](#passo-2-provisionamento-da-infraestrutura-com-terraform)
4. [Passo 3: Treinamento do Modelo com Vertex AI](#passo-3-treinamento-do-modelo-com-vertex-ai)
5. [Passo 4: Implantação Automatizada com Cloud Functions](#passo-4-implantação-automatizada-com-cloud-functions)
6. [Passo 5: Configuração de Monitoramento e Alertas](#passo-5-configuração-de-monitoramento-e-alertas)
7. [Passo 6: Testando o Pipeline](#passo-6-testando-o-pipeline)
8. [Limpeza de Recursos](#limpeza-de-recursos)
9. [Contribuição](#contribuição)

---

## Pré-requisitos

Antes de começar, você precisará:

1. **Conta na GCP**: Crie uma conta no [Google Cloud Platform](https://cloud.google.com/) e ative o billing (é necessário para usar serviços como Vertex AI e Cloud Composer).
2. **Google Cloud SDK**: Instale o [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) e configure-o com o comando `gcloud init`.
3. **Terraform**: Instale o [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli).
4. **Python 3.7+**: Instale o [Python](https://www.python.org/downloads/).
5. **Git**: Instale o [Git](https://git-scm.com/downloads).

---

## Passo 1: Configuração Inicial

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/mlops-gcp-pipeline.git
   cd mlops-gcp-pipeline

2. **Autentique-se na GCP**:
Execute o seguinte comando para autenticar sua conta:
gcloud auth login

3. **Defina o projeto GCP**:
Substitua seu-projeto-gcp pelo ID do seu projeto na GCP:
gcloud config set project seu-projeto-gcp

4. **Habilite as APIs necessárias**:
Execute os seguintes comandos para habilitar as APIs usadas no projeto:
gcloud services enable aiplatform.googleapis.com
gcloud services enable composer.googleapis.com
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable logging.googleapis.com
gcloud services enable monitoring.googleapis.com

## Passo 2: Provisionamento da Infraestrutura com Terraform

1. **Configure o Terraform**:
No diretório terraform/, crie um arquivo chamado terraform.tfvars e adicione o ID do seu projeto:
project_id = "seu-projeto-gcp"

2. **Inicialize o Terraform**:
Execute os seguintes comandos para inicializar e aplicar a configuração do Terraform:
cd terraform
terraform init
terraform apply

3. **Saídas do Terraform**:
Após a execução, o Terraform exibirá os nomes dos recursos criados, como o bucket do Cloud Storage e o ambiente do Cloud Composer. Anote esses valores, pois serão usados posteriormente.

## Passo 3: Treinamento do Modelo com Vertex AI

1. **Prepare o ambiente Python**:
No diretório raiz do projeto, crie um ambiente virtual e instale as dependências:
python3 -m venv venv
source venv/bin/activate
pip install google-cloud-aiplatform google-cloud-storage

2. **Execute o script de treinamento**:
Execute o script train_model.py para treinar o modelo:
python train_model.py

## Passo 4: Implantação Automatizada com Cloud Functions
1. **Implante a Cloud Function**:
No diretório cloud_functions/, implante a função que será acionada quando um novo modelo for registrado:
cd cloud_functions
gcloud functions deploy redeploy_model \
    --runtime python310 \
    --trigger-topic model-registry-updates \
    --entry-point redeploy_model

2. **Teste a Cloud Function**:
Registre manualmente uma nova versão do modelo no Vertex AI Model Registry e verifique se a função é acionada para implantar o modelo.

## Passo 5: Configuração de Monitoramento e Alertas
1. **Acesse o Cloud Monitoring**:
No Console da GCP, vá para Monitoring > Alertas.

2. **Crie um alerta de latência**:
* Defina a métrica como serving.googleapis.com/prediction/latency.
* Configure o limite de latência (por exemplo, 500ms).
* Adicione um canal de notificação (por exemplo, e-mail ou Pub/Sub).

3. **Verifique os logs**:
No Console da GCP, vá para Logging > Logs Explorer para visualizar os logs de treinamento e inferência.

## Passo 6: Configuração Inicial

1. **Execute o pipeline completo**:
* Treine um novo modelo com train_model.py.
* Verifique se o modelo foi registrado no Vertex AI Model Registry.
* Confirme se a Cloud Function implantou o modelo automaticamente.
* Verifique os logs e alertas no Cloud Monitoring.

2. **Teste a inferência**:
Use o endpoint do modelo implantado para fazer previsões e verificar a latência.

## Estrutura do Repositório
mlops-gcp-pipeline/
├── terraform/                  # Arquivos de configuração do Terraform
│   ├── main.tf                 # Configuração principal do Terraform
│   ├── variables.tf            # Variáveis do Terraform
│   └── outputs.tf              # Saídas do Terraform
├── cloud_functions/            # Código da Cloud Function
│   └── redeploy_model.py       # Função para reimplantar o modelo
├── scripts/                    # Scripts de treinamento e inferência
│   └── train_model.py          # Script para treinar o modelo
├── README.md                   # Este arquivo
└── requirements.txt            # Dependências do Python

## Como Usar Este Repositório
* Substitua seu-usuario pelo seu nome de usuário no GitHub/GitLab.
* Substitua seu-projeto-gcp pelo ID do seu projeto na GCP.
* Siga os passos descritos no README para implementar o pipeline.