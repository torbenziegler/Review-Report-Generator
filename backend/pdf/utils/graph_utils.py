import io
import matplotlib.pyplot as plt

def create_histogram_image(data, title, x_label, y_label):
    plt.figure(figsize=(6, 4))
    plt.hist(data, bins=10, color='blue', edgecolor='black')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return buffer
