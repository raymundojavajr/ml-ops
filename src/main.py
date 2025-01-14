"""
Main module for running the ML pipeline.
"""

import sys
import logging
from src.models import train_model
from src.data_loading import load_data
from src.utils.save_utils import save_model


def main():
    """Main function to run the ML pipeline."""
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the ML pipeline")

    try:
        file_path = "data/match_maker.xlsx"
        data = load_data(file_path)
        logging.info("Data loaded successfully")

        x_data = data.drop("target", axis=1)
        y_data = data["target"]

        model = train_model(x_data, y_data)
        save_model(model, "model.pkl")
        logging.info("Model saved successfully")

    except Exception as ex:
        logging.error("An error occurred: %s", ex)
        sys.exit(1)


if __name__ == "__main__":
    main()
