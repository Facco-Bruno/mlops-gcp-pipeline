from google.cloud import aiplatform
import functions_framework

@functions_framework.cloud_event
def redeploy_model(cloud_event):
    data = cloud_event.data

    model_id = data["message"]["attributes"]["modelId"]
    model_version = data["message"]["attributes"]["version"]

    aiplatform.init(project="seu-projeto-gcp", location="us-central1")

    model = aiplatform.Model(model_name=model_id)
    endpoint = model.deploy(
        deployed_model_display_name=f"ml-model-{model_version}",
        traffic_split={"0": 100},
        machine_type="n1-standard-4",
    )

    print(f"Model {model_id} version {model_version} deployed to {endpoint.resource_name}")