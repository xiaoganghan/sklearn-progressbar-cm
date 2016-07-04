import os
import numpy as np
from sklearn.metrics import confusion_matrix
from jinja2 import Environment, FileSystemLoader


def load_data():
    CLASSES = 10
    SIZE = 10000
    y_test = np.random.randint(0, CLASSES, size=SIZE)
    y_pred = (y_test * 4 + np.random.randint(0, CLASSES, size=SIZE)) / 5
    cm = confusion_matrix(y_test, y_pred)
    target_names = ['class_{}'.format(i) for i in range(CLASSES)]

    return cm, target_names


def report(cm, target_names):
    cm_graph_rows = []
    for label, scores in zip(target_names, cm.tolist()):
        total_score = float(sum(scores))
        if total_score > 0:
            scores = [100 * score / total_score for score in scores]
        row = [label] + scores
        cm_graph_rows.append(row)
    cm_graph = {
        'header_line': [''] + target_names,
        'rows': cm_graph_rows
    }

    data_dict = {
        'cm_graph': cm_graph
    }
    current_dir = os.path.dirname(os.path.realpath(__file__))
    env = Environment(loader=FileSystemLoader(current_dir))
    template = env.get_template('cm_tmpl.html')
    output_from_parsed_template = template.render(**data_dict)

    report_filename = 'cm.html'
    report_filepath = os.path.join(current_dir, report_filename)

    with open(report_filepath, "wb") as fh:
        fh.write(output_from_parsed_template.encode('u8'))


if __name__ == '__main__':
    cm, target_names = load_data()
    report(cm, target_names)
