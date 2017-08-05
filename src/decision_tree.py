"""The decision tree data structure."""
import pandas as pd


class Node(object):
    """Class for node object."""

    def __init__(self, axis, amount, result_one, result_two):
        """Inits the node."""
        self.axis = axis
        self.amount = amount
        self.result_one = result_one
        self.result_two = result_two


class DecisionTree(object):
    """Decision tree object."""

    def __init__(self, max_depth=10, min_leaf_size=1):
        """Inits the DTree."""
        self.root = None
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size

    def predict(self, data):
        """Return labels for test data."""
        results = []
        if type(data) in [list, tuple]:
            data = pd.DataFrame(data, columns=['petal length (cm)', 'petal width (cm)', 'sepal length (cm)', 'sepal width (cm)'])
        for row in data.iterrows():
            results.append(self.root(row))
        data['results'] = results
        return data

    def fit(self, data, depth=0):
        """A decision tree based on incoming data set."""
        b_score = float("inf")
        if type(data) in [list, tuple]:
            data = pd.DataFrame(data, columns=['petal length (cm)', 'petal width (cm)', 'sepal length (cm)', 'sepal width (cm)', 'target', 'class_names'])
        if depth == self.max_depth or len(data) < self.min_leaf_size:
            return data.mode()['class_names'].iloc[0]
        else:
            smallest_length = data["sepal length (cm)"].min()
            biggest_length = data["sepal length (cm)"].max()
        data = data.sort_values(["sepal length (cm)"])
        for i in range(int(smallest_length * 10), int(biggest_length * 10) + 1):
            left_side = data[data["sepal length (cm)"] < i / 10]
            right_side = data[data["sepal length (cm)"] >= i / 10]
            left_sum = left_side["target"].sum()
            left_score = left_sum if left_sum < (len(left_side) - left_sum) else (len(left_side) - left_sum)
            right_sum = right_side["target"].sum()
            right_score = right_sum if right_sum < (len(right_side) - right_sum) else (len(right_side) - right_sum)
            score = left_score + right_score
            if score < b_score:
                best_left_side = left_side
                best_right_side = right_side
                b_score = score
                best_axis = "sepal length (cm)"
                best_amount = i / 10
            elif score == b_score:
                if abs(len(right_side) - len(left_side)) < abs(len(best_right_side) - len(best_left_side)):
                    best_left_side = left_side
                    best_right_side = right_side
                    b_score = score
                    best_axis = "sepal length (cm)"
                    best_amount = i / 10
        else:
            smallest_width = data["sepal width (cm)"].min()
            biggest_width = data["sepal width (cm)"].max()
        data = data.sort_values(["sepal width (cm)"])
        for i in range(int(smallest_width * 10), int(biggest_width * 10) + 1):
            left_side = data[data["sepal width (cm)"] < i / 10]
            right_side = data[data["sepal width (cm)"] >= i / 10]
            left_sum = left_side["target"].sum()
            left_score = left_sum if left_sum < (len(left_side) - left_sum) else (len(left_side) - left_sum)
            right_sum = right_side["target"].sum()
            right_score = right_sum if right_sum < (len(right_side) - right_sum) else (len(right_side) - right_sum)
            score = left_score + right_score
            if score <= b_score:
                best_left_side = left_side
                best_right_side = right_side
                b_score = score
                best_axis = "sepal width (cm)"
                best_amount = i / 10
            elif score == b_score:
                if abs(len(right_side) - len(left_side)) < abs(len(best_right_side) - len(best_left_side)):
                    best_left_side = left_side
                    best_right_side = right_side
                    b_score = score
                    best_axis = "sepal width (cm)"
                    best_amount = i / 10
        left_sum = best_left_side["target"].sum()
        left_score = left_sum if left_sum < (len(best_left_side) - left_sum) else (len(best_left_side) - left_sum)
        right_sum = best_right_side["target"].sum()
        right_score = right_sum if right_sum < (len(best_right_side) - right_sum) else (len(best_right_side) - right_sum)
        if depth == 0:
            if left_score == 0 and right_score == 0:
                self.root = Node(best_axis, best_amount, best_left_side['class_names'].iloc[0], best_right_side['class_names'].iloc[0])
            elif left_score == 0:
                self.root = Node(best_axis, best_amount, best_left_side['class_names'].iloc[0], self.fit(best_right_side, depth +1))
            elif right_score == 0:
                self.root = Node(best_axis, best_amount, self.fit(best_left_side, depth + 1), best_right_side['class_names'].iloc[0])
            else:
                self.root = Node(best_axis, best_amount, self.fit(best_left_side, depth + 1), self.fit(best_right_side, depth +1))
        else:
            if left_score == 0 and right_score == 0:
                return Node(best_axis, best_amount, best_left_side['class_names'].iloc[0], best_right_side['class_names'].iloc[0])
            elif left_score == 0:
                return Node(best_axis, best_amount, best_left_side['class_names'].iloc[0], self.fit(best_right_side, depth + 1))
            elif right_score == 0:
                return Node(best_axis, best_amount, self.fit(best_left_side, depth + 1), best_right_side['class_names'].iloc[0])
            else:
                return Node(best_axis, best_amount, self.fit(best_left_side, depth + 1), self.fit(best_right_side, depth + 1))


if __name__ == '__main__':
    dimitri = DecisionTree()
    df = pd.read_csv("flowers_data.csv")
    dimitri.fit(df)
    new_data = pd.read_csv("flower2.csv")
    print(dimitri.predict(new_data))
    data = [[1, 2, 3, 4, 0, 'setosa'], [5, 4, 3, 2, 1, 'versicolor']]
    dimitri.fit(data)
    new_data = pd.read_csv("flower2.csv")
    print(dimitri.predict(new_data))
