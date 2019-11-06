from picocv._settings import Settings

class Trainer:
    def __init__(self, model_func, dataset, settings : Settings):
        self.model_func = model_func
        self.dataset = dataset
        self.settings = settings
