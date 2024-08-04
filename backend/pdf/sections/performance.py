from reportlab.platypus import Image
from pdf.utils.graph_utils import create_histogram_image

def create_performance_section(data, img_size=(290, 180)):
    width, height = img_size
    histogram_image = create_histogram_image(data['histogram'], "Performance Histogram", "tbd x", "tbd y")
    performance_chart = Image(histogram_image, width, height)
    return performance_chart