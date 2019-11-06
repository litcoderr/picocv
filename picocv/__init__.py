"""
Main Methods are declared here
"""
from picocv._settings import Settings
from picocv.utils.train import Trainer
from picocv.utils.augment import DatasetAugmenter

def autoCorrect(model_func, dataset_func, settings : Settings):
    """
    Performs Auto Correct Algorithm (Main Method)
    :param model_func: Function that returns Custom Model Class  (torch.nn.Module)
    :param dataset_func: Function that returns Custom Dataset Class  (torch.utils.data.Dataset)
    :param settings: Picocv Settings  (picocv.Settings)
    :return: None
    """
    # Validate Settings
    assert settings.validate(), 'Update to Valid Settings Variables!!'

    # Initialize Dataset Augmenter
    dataset_augmenter = DatasetAugmenter(dataset_func=dataset_func, settings=settings)

    input_string = input('\nContinue? (Y/n)')
    if input_string == 'Y':
        # Start Pico Algorithm
        for iteration in range(settings.n_iter):
            print('[{current_iteration}/{total_iteration}] Starting {current_iteration}-th Iteration...'.format(current_iteration=iteration + 1,
                                                                                                                total_iteration=settings.n_iter))
            for segment_id in range(dataset_augmenter.N_SEGMENT):
                print('Start Training Checker-[{segment_id}]'.format(segment_id=segment_id))

                segment_dataset = dataset_augmenter.get_dataset(iteration_id=iteration, segment_id=segment_id)  # returned segmented dataset
                trainer = Trainer(model_func=model_func, dataset=segment_dataset, settings=settings)  # initialize trainer

    print('finished')
