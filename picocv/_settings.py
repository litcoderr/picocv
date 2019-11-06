import os

class Settings:
    def __init__(self, result_dir, n_iter=10, n_segment=5):
        """
        Initialize Settings Variables

        :param result_dir:
        """
        # TODO (settings) update more settings variable
        self.result_dir = result_dir

        self.n_iter = n_iter
        self.n_segment = n_segment

    def validate(self):
        # TODO (settings) update validation method
        """
        Validate Settings Variables
        :return: validity (boolean)
        """
        print("Start Settings Validation...")
        is_valid = True

        # check [result_dir]
        if not os.path.exists(self.result_dir):
            os.mkdir(self.result_dir)


        self.print_settings()
        print("Finished Settings Validation...")
        return is_valid

    def print_settings(self):
        print("-------------------------------------")
        print("result_dir: {result_dir}".format(result_dir=self.result_dir))
        print("n_iter: {n_iter}".format(n_iter=self.n_iter))
        print("n_segment: {n_segment}".format(n_segment=self.n_segment))
        print("-------------------------------------")

