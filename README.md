# 🏷️ names2usernames

`names2usernames` is a **Python 3** script designed to transform real names into the most common corporate username conventions.

---

## 🚀 Features

* **Common Conventions:** Automatically generates 3 popular username formats per input:
  * `firstName.lastName` (e.g., `sergio.guijarro`)
  * `firstInitialLastName` (e.g., `sguijarro`)
  * `firstNameLastInitial` (e.g., `sergiog`)
* **Bulk Processing:** Reads and parses large wordlists of names from a plain text file.
* **Randomization:** Includes an option to randomize the generated username list (`-r`).
* **File Output:** Saves generated usernames directly to an output file (`-o`).

---

## ⚙️ Usage & Arguments

You can display the built-in help menu at any time by running:

```bash
python3 names2usernames.py -h
```

### Available Arguments

| Short Flag | Long Flag | Description |
| :--- | :--- | :--- |
| `-u` | `--username` | Single name input to transform (e.g., `"John Doe"`). |
| `-f` | `--file` | Path to a text file containing names (one per line). |
| `-r` | `--random` | Randomizes the order of the generated usernames. |
| `-o` | `--output` | Saves the output to a specified file. |

---

## 💡 Examples

### 1. Convert a single name
```bash
python3 names2usernames.py -u "Sergio Guijarro"
```

### 2. Process a file and export the output
```bash
python3 names2usernames.py -f names.txt -o usernames.txt
```

### 3. Generate randomized usernames from a file
```bash
python3 names2usernames.py -f names.txt -r
```

---
