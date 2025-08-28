from flask import Flask, request, jsonify, render_template
from binDB.smartdb import SmartBinDB

app = Flask(__name__)
db = SmartBinDB()

# API ক্রেডিটের তথ্য
API_CREDITS = {
    "API Owner": "@no_coder_pro",
    "API Channel": "@no_coder_xone"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/bin/<string:bin_number>', methods=['GET'])
def get_bin_info_api(bin_number):
    result = db.get_bin_info(bin_number)
    result.update(API_CREDITS) # ফলাফলের সাথে ক্রেডিটের তথ্য যোগ করা হলো
    return jsonify(result)

@app.route('/api/bank/<string:bank_name>', methods=['GET'])
def get_bins_by_bank_api(bank_name):
    limit = request.args.get('limit', type=int)
    result = db.get_bins_by_bank(bank_name, limit)
    result.update(API_CREDITS) # ফলাফলের সাথে ক্রেডিটের তথ্য যোগ করা হলো
    return jsonify(result)

@app.route('/api/country/<string:country_code>', methods=['GET'])
def get_bins_by_country_api(country_code):
    # ইউজার limit নিলাম (ডিফল্ট = 20)
    limit = request.args.get('limit', type=int, default=20)

    # যদি limit > 20 হয় তাহলে শুধু মেসেজ পাঠাবে
    if limit > 20:
        return jsonify({
            "error": "সর্বোচ্চ 20 টা পর্যন্ত রেজাল্ট নেওয়া যাবে। অনুগ্রহ করে 20 বা তার কম ব্যবহার করুন।",
            **API_CREDITS
        }), 400  # Bad Request

    # নাহলে ডাটাবেজ থেকে limit সংখ্যক ডেটা রিটার্ন করবে
    result = db.get_bins_by_country(country_code, limit)
    result.update(API_CREDITS)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

