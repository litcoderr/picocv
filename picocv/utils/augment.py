from picocv._settings import Settings

import os
import json


class DatasetAugmenter:
    def __init__(self, dataset_func, settings: Settings):
        self.dataset_func = dataset_func
        self.settings = settings

        assert self.validate(), "Dataset Augmenter Error"

        # HELPER OBJECTS #
        self.label_augmenter = LabelAugmenter(dataset_func=dataset_func, settings=settings)

        # VARIABLES #
        self.N_SEGMENT = self.settings.n_segment

    def validate(self):
        is_valid = True
        validation_dataset = self.dataset_func()

        # Check if n_segment is valid
        dataset_len = len(validation_dataset)
        if dataset_len < self.settings.n_segment:
            print("Dataset Augmenter Error: Too much number of segments")
            is_valid = False

        return is_valid

    def get_dataset(self, iteration_id, segment_id):
        base_dataset = self.dataset_func()
        label_iterator = self.label_augmenter.get_label_iterator(iteration_id=iteration_id)

        # TODO Augment dataset with corresponding segment id
        return base_dataset


class LabelAugmenter:
    def __init__(self, dataset_func, settings: Settings):
        self.dataset_func = dataset_func
        self.settings = settings

        # Initialize iteration-0 label file
        print('Initializing Label...')
        file_name = self.get_file_name(iteration=0)
        extracted_label = {}
        temp_dataset = self.dataset_func()
        for index, (_, label) in enumerate(temp_dataset):
            temp_label = int(label.cpu().numpy()[0])
            extracted_label[index] = temp_label
        del temp_dataset
        with open(file_name, 'w') as file:
            json.dump(extracted_label, file)

    def get_label_iterator(self, iteration_id):
        file_name = self.get_file_name(iteration=iteration_id)
        return LabelIterator(file_name=file_name)

    # HELPER METHODS
    def get_file_name(self, iteration):
        n_length = len(str(self.settings.n_iter))
        return os.path.join(self.settings.result_dir, 'iter_{iteration}.json'.format(iteration=str(iteration).zfill(n_length)))


class LabelIterator:
    # TODO Finish Label Iterator
    def __init__(self, file_name):
        self.file_name = file_name
        print("Loading Label...")
        self.label = {}
        with open(self.file_name, 'r') as file:
            self.label = json.load(file)
            file.close()
        self.dataset_length = len(self.label)

    def get(self, index):
        if index < self.dataset_length:
            return self.label[str(index)]
        else:
            print('Invalid index: {index} with dataset_length: {dataset_length}'.format(index=index, dataset_length=self.dataset_length))
            return None