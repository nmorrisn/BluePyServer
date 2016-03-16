import JSON

class getJSONObject:

    def jsonify(self,results):
        jsonResults = json.dumps({'Glucose level (mg/L)' : results}, indent=4)
        print(jsonResults)
        return jsonResults
