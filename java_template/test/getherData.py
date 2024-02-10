import pandas as pd
import json
import xml.etree.ElementTree as ET

# responseOutput.xmlファイルのパス
xml_file_path = '/Users/tkondo/Desktop/FreeWorkspace/JMeter/apache-jmeter-5.6.3/bin/responseOutput.xml'

# XMLファイルを読み込む
tree = ET.parse(xml_file_path)
root = tree.getroot()

# XMLデータを表示
xml_data = ET.tostring(root, encoding='utf-8').decode('utf-8')
print(xml_data)

result_data = []
for http_sample in root.findall(".//httpSample"):
    response_data_str = http_sample.find("responseData").text
    response_data_json = json.loads(response_data_str)
    result_data.append(response_data_json)
print(json.dumps(result_data, indent=2))
df = pd.json_normalize(result_data)
df.to_csv('output.csv',index = False)
