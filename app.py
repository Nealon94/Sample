from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)

# Path to your XML file in the project directory
xml_file_path = os.path.join(os.path.dirname(__file__), 'Pavan Lalwani Sales Report.xml')

@app.route('/extract-data', methods=['GET'])
def extract_data():
    try:
        # Serve the XML file
        return send_file(xml_file_path, mimetype='application/xml')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
