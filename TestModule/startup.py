
import argparse

import ImageAnalysisModel as pa


def main(image_folder_path, containerWidth,config_path):
    """
    Main function to execute the image analysis process.
    """
    analyser = pa.ImageAnalysisModel(image_folder_path, containerWidth=containerWidth, config_path=config_path)
    analyser.run_analysis()

    # if not image_folder_path or not containerWidth:
    #     print("Please provide image folder path as well as the container width.")
    #     return
    # # Read configuration
    # config = configparser.ConfigParser()
    # config.read(config_path)
    #
    # # Retrieve bins from config file
    # industry_bins_string = config['analysis']['industryBin']
    # bins = parse_bins(industry_bins_string)
    # if not bins:
    #     industry_standard_bins = [38, 106, 1000, 8000]  # bins
    # else:
    #     industry_standard_bins=bins[:]
    #
    # # Retrieve configuration settings for reminder area
    # calculated_reminder_area = int(config.get('switch', 'CalculatedAdjustedBins_Area', fallback='0'))
    #
    # # Retrieve configuration settings for advanced bin calculations
    # calculated_size = int(config.get('switch', 'CalculatedAdjustedBins_Size', fallback='0'))
    # calculated_area = int(config.get('switch', 'CalculatedAdjustedBins_Area', fallback='0'))
    # target_distribution = eval(config.get('PSD', 'lab', fallback='[]'))
    #
    # #normal bins
    # normal_bins = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    #
    # # Checkpoint folder
    # checkpoint_folder = 'checkpoints'
    # model_url = 'https://dl.fbaipublicfiles.com/segment_anything_2/092824/sam2.1_hiera_large.pt'
    # model_name = 'sam2.1_hiera_large.pt'
    # download_model(checkpoint_folder, model_url, model_name)
    #
    # ########################### Begin Analyzing #####################################
    # analyser = pa.ImageAnalysisModel(image_folder_path, containerWidth=containerWidth)
    # analyser.evenLighting()
    # analyser.overlayImage()
    # Testing = False
    # analyser.analyseParticles(checkpoint_folder, Testing)
    # analyser.saveSegments()
    #
    #
    # # analyser.saveResults(industry_standard_bins)
    # analyser.setBins(industry_standard_bins)
    # analyser.savePsdData()
    #
    # if calculated_reminder_area == 1:
    #     analyser.loadCalibrator()
    #     analyser.calculate_unsegmented_area()
    #     analyser.calibrated_bins_with_unSegementedArea()
    #     analyser.refactor_psd()
    #     distribution_fileName = os.path.join(analyser.folder_path, f'{analyser.sampleID}_refactored_distribution.txt')
    #     analyser.formatResults(byArea=True, distribution_filename=distribution_fileName)
    # else:
    #     analyser.saveDistributionPlot()
    #     analyser.formatResults(byArea=True)
    #
    # analyser.savePsdDataWithDiameter()
    # analyser.formatResults(bySize=True)
    # analyser.saveDistributionPlotForDiameter()
    #
    # analyser.saveResultsForNormalBinsOnly(normal_bins)
    # analyser.formatResultsForNormalDistribution(True)
    #
    #
    # # Decide based on configuration which advanced analysis to run
    # if target_distribution:
    #     if calculated_size == 1:
    #         print("Calculating bins by size...")
    #         analyser.calibrate_bin_with_size(target_distribution)
    #     if calculated_area == 1:
    #         print("Calculating bins by area...")
    #         analyser.calibrate_bin_with_area(target_distribution)
    # else:
    #     print("No target distribution provided. Skipping advanced bin calculations.")

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run particle analysis on the provided image folder.")
    parser.add_argument('image_folder_path', type=str, help='Path to the folder containing sample images.')
    parser.add_argument('--containerWidth', default=180000,type=int,help='Container width in micrometers, for example, 18 cm is equal to 180000 µm.')
    parser.add_argument('--config_path', type=str, default='config.ini',
                        help='config file path')
    args = parser.parse_args()

    main(args.image_folder_path,args.containerWidth,args.config_path)

