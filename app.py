from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)

# Path to your XML file (relative path)
xml_file_path = os.path.join('data', 'Pavan Lalwani Sales Report.xml')

@app.route('/extract-data', methods=['GET'])
def extract_data():
    try:
        # Serve the XML file
        return send_file(xml_file_path, mimetype='application/xml')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
