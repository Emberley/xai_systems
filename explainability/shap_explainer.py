import shap

def explain(model, data):
    explainer = shap.Explainer(model)
    return explainer(data)
