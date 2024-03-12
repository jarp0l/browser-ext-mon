import os

import joblib

models_dir = os.path.join(os.path.dirname(__file__), "models")


class ModelLoader:
    def __init__(self, models_dir: str = models_dir):
        self.models_dir = models_dir

    def get_all_models(self):
        """
        Get a list of all available model files in the specified directory.

        Returns:
            List of model filenames.
        """
        model_files = [f for f in os.listdir(self.models_dir) if f.endswith(".pkl")]
        return model_files

    def load_model(self, model_name):
        """
        Load a pre-trained machine learning model.

        **Do not** include .pkl extension with model_name.

        Args:
            model_name (str): The name (without .pkl extension) of the model to load.

        Returns:
            The loaded machine learning model.
        """
        model_path = os.path.join(self.models_dir, f"{model_name}.pkl")
        model = joblib.load(model_path)
        return model

    def load_all_models(self):
        """
        Load all pre-trained machine learning models.

        Returns:
            A dictionary where keys are model names and values are the loaded models.
        """
        model_names = [os.path.splitext(f)[0] for f in self.get_all_models()]
        loaded_models = {}

        for model_name in model_names:
            loaded_models[model_name] = self.load_model(model_name)

        return loaded_models


if __name__ == "__main__":
    model_loader = ModelLoader()
    models = model_loader.get_all_models()
    print(models)
