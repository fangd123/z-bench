import requests
import csv
import json

def call_api(prompt, history):
    url = "http://127.0.0.1:8000"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": prompt, "history": history}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.json()

def read_csv(file_path):
    prompts = []
    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            prompts.append(row[0])  # Assuming "Prompt" is the first column
    return prompts

def write_csv(file_path, data):
    with open(file_path, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Prompt", "Response"])
        for item in data:
            writer.writerow(item)

if __name__ == "__main__":
    input_csv = "specialized.samples.csv"
    output_csv = "specialized.samples.output.csv"

    #input_csv = "emergent.samples.csv"
    #output_csv = "emergent.samples.output.csv"
    prompts = read_csv(input_csv)
    result_data = []

    for prompt in prompts:
        response = call_api(prompt, [])
        result_data.append([prompt, response["response"]])

    write_csv(output_csv, result_data)
