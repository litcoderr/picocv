"""
Main Methods are declared here
"""
from picocv._settings import Settings

def autoCorrect(model, dataset, settings : Settings):
    """
    Performs Auto Correct Algorithm (Main Method)
    ----------------------[Usage]--------------------------
    import picocv  # Import picocv
    import MyModel  # Import Custom Model
    import MyDataset  # Import Custom Dataset

    settings = picocv.Settings() # Initialize settings

    picocv.autoCorrect(MyModel, MyDataset, settings)
    -------------------------------------------------------

    :param model: Custom Model Class  (torch.nn.Module)
    :param dataset: Custom Dataset Class  (torch.utils.data.Dataset)
    :param settings: Picocv Settings  (picocv.Settings)
    :return: None
    """
    # Validate Settings
    assert settings.validate(), "Update to Valid Settings Variables!!"

    # TODO (main) implement pico algorithm
    pass