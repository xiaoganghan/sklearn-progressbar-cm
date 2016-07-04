import os
from jinja2 import Environment, FileSystemLoader


def generate_data(cm, target_names):
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
    return cm_graph


def generate_report(cm, target_names, report_filepath='cm.html'):
    cm_graph = generate_data(cm, target_names)

    data_dict = {
        'cm_graph': cm_graph
    }
    current_dir = os.path.dirname(os.path.realpath(__file__))
    env = Environment(loader=FileSystemLoader(current_dir))
    template = env.get_template('cm_tmpl.html')
    output_from_parsed_template = template.render(**data_dict)

    with open(report_filepath, "wb") as fh:
        fh.write(output_from_parsed_template.encode('u8'))


if __name__ == '__main__':
    pass
