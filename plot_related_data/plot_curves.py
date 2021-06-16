import matplotlib.pyplot as plt
import sys
import os



def _parse_input(filename):
    ''' Private function that parses the input of a input file if it satisfies the specified format'''
    content = _get_file_content(filename)
    curves_content = content.split('*')
    curve_titles = list()
    curves = list()
    for curve in curves_content[1:]:
        single_curve = list()
        lines = curve.split('-')
        curve_titles.append(lines[0].strip('\n'))
        for line in lines[1:]:
            appendix = line.split(':')[1].strip()
            single_curve.append(float(appendix))
        curves.append(single_curve)
    return(curve_titles, curves)

def _get_file_content(filename):
    ''' Private function that reads in the input file'''
    try:
        f = open(filename, 'r')
        content = f.read()
        return content
    except FileNotFoundError:
        print(f"Given file '{filename}' was not found")
        sys.exit(1)

def _prorduce_input_dependend_line_plot(title_list, curve_list, plot_title, output_file_name, start_input_size, input_step_size, y_axis_title, x_axis_title):
    input_size_vec = range(start_input_size, len(curve_list[0])*start_input_size + start_input_size, input_step_size)
    y_axis = y_axis_title if y_axis_title is not None else "Execution time [s]"
    for curve in curve_list:
        plt.plot(input_size_vec, curve)
        plt.scatter(input_size_vec, curve, marker='x')
    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis)
    plt.legend(title_list)
    plt.title(plot_title)
    _create_folder_for_graphics()
    plt.savefig("./plots/" + output_file_name)
    plt.clf()

def _create_folder_for_graphics():
    '''Private function that generates the folder ./plots if it doesnt already exist'''

    if not os.path.exists('./plots'):
        os.makedirs('./plots')

titles, curves = _parse_input("accuracies.txt")
_prorduce_input_dependend_line_plot(titles, curves, "Accuracies per epoch", "accuracy", 1, 1, "accuracy", "Number of epochs")
titles, curves = _parse_input("loss.txt")
_prorduce_input_dependend_line_plot(titles, curves, "Loss per epoch", "loss", 1, 1, "loss", "Number of epochs")