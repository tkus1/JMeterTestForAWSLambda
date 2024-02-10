#!/bin/bash

# ターゲットのエンドポイントURL
#url="https://zsig8n5oog.execute-api.us-east-2.amazonaws.com/Deploy"
url="3.16.88.178/Deploy"

# 送信するJSONデータ
json_data='{"name": "userName31411", "key2": "value2"}'

# CurlコマンドでPOSTリクエストを送信
curl -X POST -H "Content-Type: application/json" -d "$json_data" "$url" -o "outputJSON.json"
