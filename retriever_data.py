import matplotlib.pyplot as plt


def retrieve_data():
    file_path = "./last_tests/sgd.txt"

    values = {
        "train_loss": [],
        "val_loss": [],
        "train_acc": [],
        "val_acc": [],
        "best_epoch": None,
    }

    res = {}

    with open(file_path, "r") as file:
        current_test = None
        for line in file:
            if line.startswith("#"):
                if current_test:
                    res[current_test] = values = {
                        "train_loss": [],
                        "val_loss": [],
                        "train_acc": [],
                        "val_acc": [],
                        "best_epoch": None,
                    }  # Creazione di nuove liste per ogni test
                    res[current_test]["train_loss"].extend(train_loss_values)
                    res[current_test]["val_loss"].extend(val_loss_values)
                    res[current_test]["train_acc"].extend(train_acc_values)
                    res[current_test]["val_acc"].extend(val_acc_values)
                    res[current_test]["best_epoch"] = best_epoch

                print(values)
                current_test = " ".join(line.split()[1:])
                train_loss_values = []
                val_loss_values = []
                train_acc_values = []
                val_acc_values = []
                best_epoch = None
            elif "Train loss is" in line:
                train_loss = float(line.split()[-1])
                train_loss_values.append(train_loss)
            elif "Validation Loss:" in line:
                val_loss = float(line.split(":")[-1].strip())
                val_loss_values.append(val_loss)
            elif "Training acc is" in line:
                train_acc = float(line.split()[-1].strip("%")) / 100
                train_acc_values.append(train_acc)
            elif "Validation acc is" in line:
                val_acc = float(line.split()[-1].strip("%")) / 100
                val_acc_values.append(val_acc)
            elif "Best epoch:" in line:
                best_epoch = int(line.split()[-1])

        # Aggiunta dei valori per l'ultimo test
        if current_test:
            res[current_test] = values.copy()
            res[current_test]["train_loss"].extend(train_loss_values)
            res[current_test]["val_loss"].extend(val_loss_values)
            res[current_test]["train_acc"].extend(train_acc_values)
            res[current_test]["val_acc"].extend(val_acc_values)
            res[current_test]["best_epoch"] = best_epoch
    return res


def plot_values(values, title, ylabel, xlabel, legend):
    plt.figure(figsize=(5, 7))
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    plt.ylim(0, 2.1)
    plt.yticks([i / 5 for i in range(11)])
    for k, v in values.items():
        plt.plot(v, label=k)
        if k == "best_epoch":
            plt.axvline(x=v, ymax=0.6, color="red", linestyle="--", linewidth=2)
            plt.text(
                v, 1.3, f"Best", ha="center", fontdict={"size": 12, "color": "red"}
            )

    plt.legend(legend)
    plt.savefig(f"./plots/sgd/{title}.png", dpi=300)


if __name__ == "__main__":
    res = retrieve_data()
    legend = [
        "Training Loss",
        "Validation Loss",
        "Training Accuracy",
        "Validation Accuracy",
    ]
    for k in res.keys():
        plot_values(
            res[k],
            f"SGD batch_size:64 lr: {k.split(';')[1]}",
            "",
            "Epoch",
            legend,
        )
