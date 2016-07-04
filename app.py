import numpy as np
from sklearn.metrics import confusion_matrix
from cm import report


def load_data():
    CLASSES = 10
    SIZE = 10000
    y_test = np.random.randint(0, CLASSES, size=SIZE)
    y_pred = (y_test * 4 + np.random.randint(0, CLASSES, size=SIZE)) / 5
    cm = confusion_matrix(y_test, y_pred)
    target_names = ['class_{}'.format(i) for i in range(CLASSES)]
    return cm, target_names


def generate_report():
    cm, target_names = load_data()
    report(cm, target_names)


if __name__ == '__main__':
    generate_report()
