from flask import Flask, request, jsonify, render_template
import subprocess
import os
import json

app = Flask(__name__)

# Define the script files to run in order
scripts = ["dataGathering.py", "dataCleaning.py", "categorizeData.py"]

# Serve the index.html file at the root
@app.route('/')
def serve_index():
    return render_template('index.html')  # Flask automatically looks inside the 'templates' folder

# Define the /start-process route
@app.route('/start-process', methods=['GET'])
def start_process():
    try:
        # Run each script in the defined order
        for script in scripts:
            subprocess.run(["python", script], check=True)
        
        return jsonify({"success": True, "message": "All scripts ran successfully!"})
    
    except subprocess.CalledProcessError as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Define the /save-data endpoint
@app.route('/save-data', methods=['POST'])
def save_data():
    try:
        # Parse the JSON data sent in the request
        data = request.json
        filename = data.get('filename')
        job_data = data.get('data')

        if not filename or not job_data:
            return jsonify({"success": False, "message": "Filename or data is missing."}), 400

        # Define the directory and file path
        save_directory = "./prevData"
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        
        # Save the data to the specified location
        file_path = os.path.join(save_directory, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(job_data, f, ensure_ascii=False, indent=4)
        
        return jsonify({"success": True, "message": f"Data saved successfully to {file_path}!"})
    
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
