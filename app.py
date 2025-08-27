from flask import Flask, request, jsonify
from binDB.smartdb import SmartBinDB

app = Flask(__name__)
db = SmartBinDB()

@app.route('/')
def home():
    return jsonify({
        "status": "SUCCESS",
        "message": "Welcome to binDB API. Use /api/bin, /api/bank, or /api/country endpoints.",
        "api_owner": "@ISmartCoder",
        "api_channel": "@TheSmartDev"
    })

@app.route('/api/bin/<string:bin_number>', methods=['GET'])
def get_bin_info_api(bin_number):
    result = db.get_bin_info(bin_number)
    return jsonify(result)

@app.route('/api/bank/<string:bank_name>', methods=['GET'])
def get_bins_by_bank_api(bank_name):
    limit = request.args.get('limit', type=int)
    result = db.get_bins_by_bank(bank_name, limit)
    return jsonify(result)

@app.route('/api/country/<string:country_code>', methods=['GET'])
def get_bins_by_country_api(country_code):
    limit = request.args.get('limit', type=int)
    result = db.get_bins_by_country(country_code, limit)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
