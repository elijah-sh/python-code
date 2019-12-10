CONFIG = {
    "scale": {
        "columns": ["date", "company", "mcc", "cardType", "range", "amount", "number"],
        "target_columns": ["amount", "number"],
        "date_column": "date",
        "date_format": "%Y年%m月"
    },
    "income": {
        "columns": ["date", "company", "mcc", "cardType", "range", "commission", "brand"],
        "target_columns": ["brand", "commission"],
        "date_column": "date",
        "date_format": "%Y年%m月"
    },
    "forecast": {
        "amount_columns": ['10000元以下',
                           '10000元以下_01标准类',
                           '10000元以下_02优惠类',
                           '10000元以下_03减免类',
                           '10000元以下_04特殊类',
                           '10000元以下_01标准类_黑龙江分公司',
                           '10000元以下_01标准类_辽宁分公司',
                           '10000元以下_01标准类_青海分公司',
                           '10000元以下_01标准类_四川分公司',
                           '10000元以下_01标准类_大连分公司',
                           '10000元以下_01标准类_浙江分公司',
                           '10000元以下_01标准类_吉林分公司',
                           '10000元以下_01标准类_福建分公司',
                           '10000元以下_01标准类_河北分公司',
                           '10000元以下_01标准类_宁波分公司',
                           '10000元以下_01标准类_安徽分公司',
                           '10000元以下_01标准类_广东分公司',
                           '10000元以下_01标准类_宁夏分公司',
                           '10000元以下_01标准类_江西分公司',
                           '10000元以下_01标准类_青岛分公司',
                           '10000元以下_01标准类_上海分公司',
                           '10000元以下_01标准类_深圳分公司',
                           '10000元以下_01标准类_甘肃分公司',
                           '10000元以下_01标准类_海南分公司',
                           '10000元以下_01标准类_北京分公司',
                           '10000元以下_01标准类_云南分公司',
                           '10000元以下_01标准类_山东分公司',
                           '10000元以下_01标准类_重庆分公司',
                           '10000元以下_01标准类_广西分公司',
                           '10000元以下_01标准类_贵州分公司',
                           '10000元以下_01标准类_厦门分公司',
                           '10000元以下_01标准类_新疆分公司',
                           '10000元以下_01标准类_湖北分公司',
                           '10000元以下_01标准类_湖南分公司',
                           '10000元以下_01标准类_内蒙分公司',
                           '10000元以下_01标准类_天津分公司',
                           '10000元以下_01标准类_山西分公司',
                           '10000元以下_01标准类_西藏分公司',
                           '10000元以下_01标准类_江苏分公司',
                           '10000元以下_01标准类_陕西分公司',
                           '10000元以下_01标准类_河南分公司',
                           '10000元以下_02优惠类_黑龙江分公司',
                           '10000元以下_02优惠类_辽宁分公司',
                           '10000元以下_02优惠类_青海分公司',
                           '10000元以下_02优惠类_四川分公司',
                           '10000元以下_02优惠类_大连分公司',
                           '10000元以下_02优惠类_浙江分公司',
                           '10000元以下_02优惠类_吉林分公司',
                           '10000元以下_02优惠类_福建分公司',
                           '10000元以下_02优惠类_河北分公司',
                           '10000元以下_02优惠类_宁波分公司',
                           '10000元以下_02优惠类_安徽分公司',
                           '10000元以下_02优惠类_广东分公司',
                           '10000元以下_02优惠类_宁夏分公司',
                           '10000元以下_02优惠类_江西分公司',
                           '10000元以下_02优惠类_青岛分公司',
                           '10000元以下_02优惠类_上海分公司',
                           '10000元以下_02优惠类_深圳分公司',
                           '10000元以下_02优惠类_甘肃分公司',
                           '10000元以下_02优惠类_海南分公司',
                           '10000元以下_02优惠类_北京分公司',
                           '10000元以下_02优惠类_云南分公司',
                           '10000元以下_02优惠类_山东分公司',
                           '10000元以下_02优惠类_重庆分公司',
                           '10000元以下_02优惠类_广西分公司',
                           '10000元以下_02优惠类_贵州分公司',
                           '10000元以下_02优惠类_厦门分公司',
                           '10000元以下_02优惠类_新疆分公司',
                           '10000元以下_02优惠类_湖北分公司',
                           '10000元以下_02优惠类_湖南分公司',
                           '10000元以下_02优惠类_内蒙分公司',
                           '10000元以下_02优惠类_天津分公司',
                           '10000元以下_02优惠类_山西分公司',
                           '10000元以下_02优惠类_西藏分公司',
                           '10000元以下_02优惠类_江苏分公司',
                           '10000元以下_02优惠类_陕西分公司',
                           '10000元以下_02优惠类_河南分公司',
                           '10000元以下_03减免类_黑龙江分公司',
                           '10000元以下_03减免类_辽宁分公司',
                           '10000元以下_03减免类_青海分公司',
                           '10000元以下_03减免类_四川分公司',
                           '10000元以下_03减免类_大连分公司',
                           '10000元以下_03减免类_浙江分公司',
                           '10000元以下_03减免类_吉林分公司',
                           '10000元以下_03减免类_福建分公司',
                           '10000元以下_03减免类_河北分公司',
                           '10000元以下_03减免类_宁波分公司',
                           '10000元以下_03减免类_安徽分公司',
                           '10000元以下_03减免类_广东分公司',
                           '10000元以下_03减免类_宁夏分公司',
                           '10000元以下_03减免类_江西分公司',
                           '10000元以下_03减免类_青岛分公司',
                           '10000元以下_03减免类_上海分公司',
                           '10000元以下_03减免类_深圳分公司',
                           '10000元以下_03减免类_甘肃分公司',
                           '10000元以下_03减免类_海南分公司',
                           '10000元以下_03减免类_北京分公司',
                           '10000元以下_03减免类_云南分公司',
                           '10000元以下_03减免类_山东分公司',
                           '10000元以下_03减免类_重庆分公司',
                           '10000元以下_03减免类_广西分公司',
                           '10000元以下_03减免类_贵州分公司',
                           '10000元以下_03减免类_厦门分公司',
                           '10000元以下_03减免类_新疆分公司',
                           '10000元以下_03减免类_湖北分公司',
                           '10000元以下_03减免类_湖南分公司',
                           '10000元以下_03减免类_内蒙分公司',
                           '10000元以下_03减免类_天津分公司',
                           '10000元以下_03减免类_山西分公司',
                           '10000元以下_03减免类_西藏分公司',
                           '10000元以下_03减免类_江苏分公司',
                           '10000元以下_03减免类_陕西分公司',
                           '10000元以下_03减免类_河南分公司',
                           '10000元以下_04特殊类_黑龙江分公司',
                           '10000元以下_04特殊类_辽宁分公司',
                           '10000元以下_04特殊类_青海分公司',
                           '10000元以下_04特殊类_四川分公司',
                           '10000元以下_04特殊类_大连分公司',
                           '10000元以下_04特殊类_浙江分公司',
                           '10000元以下_04特殊类_吉林分公司',
                           '10000元以下_04特殊类_福建分公司',
                           '10000元以下_04特殊类_河北分公司',
                           '10000元以下_04特殊类_宁波分公司',
                           '10000元以下_04特殊类_安徽分公司',
                           '10000元以下_04特殊类_广东分公司',
                           '10000元以下_04特殊类_宁夏分公司',
                           '10000元以下_04特殊类_江西分公司',
                           '10000元以下_04特殊类_青岛分公司',
                           '10000元以下_04特殊类_上海分公司',
                           '10000元以下_04特殊类_深圳分公司',
                           '10000元以下_04特殊类_甘肃分公司',
                           '10000元以下_04特殊类_海南分公司',
                           '10000元以下_04特殊类_北京分公司',
                           '10000元以下_04特殊类_云南分公司',
                           '10000元以下_04特殊类_山东分公司',
                           '10000元以下_04特殊类_重庆分公司',
                           '10000元以下_04特殊类_广西分公司',
                           '10000元以下_04特殊类_贵州分公司',
                           '10000元以下_04特殊类_厦门分公司',
                           '10000元以下_04特殊类_新疆分公司',
                           '10000元以下_04特殊类_湖北分公司',
                           '10000元以下_04特殊类_湖南分公司',
                           '10000元以下_04特殊类_内蒙分公司',
                           '10000元以下_04特殊类_天津分公司',
                           '10000元以下_04特殊类_山西分公司',
                           '10000元以下_04特殊类_西藏分公司',
                           '10000元以下_04特殊类_江苏分公司',
                           '10000元以下_04特殊类_陕西分公司',
                           '10000元以下_04特殊类_河南分公司'],
        "number_columns": ['10000元以上',
                           '10000元以上_01标准类',
                           '10000元以上_02优惠类',
                           '10000元以上_03减免类',
                           '10000元以上_04特殊类',
                           '10000元以上_01标准类_黑龙江分公司',
                           '10000元以上_01标准类_辽宁分公司',
                           '10000元以上_01标准类_青海分公司',
                           '10000元以上_01标准类_四川分公司',
                           '10000元以上_01标准类_大连分公司',
                           '10000元以上_01标准类_浙江分公司',
                           '10000元以上_01标准类_吉林分公司',
                           '10000元以上_01标准类_福建分公司',
                           '10000元以上_01标准类_河北分公司',
                           '10000元以上_01标准类_宁波分公司',
                           '10000元以上_01标准类_安徽分公司',
                           '10000元以上_01标准类_广东分公司',
                           '10000元以上_01标准类_宁夏分公司',
                           '10000元以上_01标准类_江西分公司',
                           '10000元以上_01标准类_青岛分公司',
                           '10000元以上_01标准类_上海分公司',
                           '10000元以上_01标准类_深圳分公司',
                           '10000元以上_01标准类_甘肃分公司',
                           '10000元以上_01标准类_海南分公司',
                           '10000元以上_01标准类_北京分公司',
                           '10000元以上_01标准类_云南分公司',
                           '10000元以上_01标准类_山东分公司',
                           '10000元以上_01标准类_重庆分公司',
                           '10000元以上_01标准类_广西分公司',
                           '10000元以上_01标准类_贵州分公司',
                           '10000元以上_01标准类_厦门分公司',
                           '10000元以上_01标准类_新疆分公司',
                           '10000元以上_01标准类_湖北分公司',
                           '10000元以上_01标准类_湖南分公司',
                           '10000元以上_01标准类_内蒙分公司',
                           '10000元以上_01标准类_天津分公司',
                           '10000元以上_01标准类_山西分公司',
                           '10000元以上_01标准类_西藏分公司',
                           '10000元以上_01标准类_江苏分公司',
                           '10000元以上_01标准类_陕西分公司',
                           '10000元以上_01标准类_河南分公司',
                           '10000元以上_02优惠类_黑龙江分公司',
                           '10000元以上_02优惠类_辽宁分公司',
                           '10000元以上_02优惠类_青海分公司',
                           '10000元以上_02优惠类_四川分公司',
                           '10000元以上_02优惠类_大连分公司',
                           '10000元以上_02优惠类_浙江分公司',
                           '10000元以上_02优惠类_吉林分公司',
                           '10000元以上_02优惠类_福建分公司',
                           '10000元以上_02优惠类_河北分公司',
                           '10000元以上_02优惠类_宁波分公司',
                           '10000元以上_02优惠类_安徽分公司',
                           '10000元以上_02优惠类_广东分公司',
                           '10000元以上_02优惠类_宁夏分公司',
                           '10000元以上_02优惠类_江西分公司',
                           '10000元以上_02优惠类_青岛分公司',
                           '10000元以上_02优惠类_上海分公司',
                           '10000元以上_02优惠类_深圳分公司',
                           '10000元以上_02优惠类_甘肃分公司',
                           '10000元以上_02优惠类_海南分公司',
                           '10000元以上_02优惠类_北京分公司',
                           '10000元以上_02优惠类_云南分公司',
                           '10000元以上_02优惠类_山东分公司',
                           '10000元以上_02优惠类_重庆分公司',
                           '10000元以上_02优惠类_广西分公司',
                           '10000元以上_02优惠类_贵州分公司',
                           '10000元以上_02优惠类_厦门分公司',
                           '10000元以上_02优惠类_新疆分公司',
                           '10000元以上_02优惠类_湖北分公司',
                           '10000元以上_02优惠类_湖南分公司',
                           '10000元以上_02优惠类_内蒙分公司',
                           '10000元以上_02优惠类_天津分公司',
                           '10000元以上_02优惠类_山西分公司',
                           '10000元以上_02优惠类_西藏分公司',
                           '10000元以上_02优惠类_江苏分公司',
                           '10000元以上_02优惠类_陕西分公司',
                           '10000元以上_02优惠类_河南分公司',
                           '10000元以上_03减免类_黑龙江分公司',
                           '10000元以上_03减免类_辽宁分公司',
                           '10000元以上_03减免类_青海分公司',
                           '10000元以上_03减免类_四川分公司',
                           '10000元以上_03减免类_大连分公司',
                           '10000元以上_03减免类_浙江分公司',
                           '10000元以上_03减免类_吉林分公司',
                           '10000元以上_03减免类_福建分公司',
                           '10000元以上_03减免类_河北分公司',
                           '10000元以上_03减免类_宁波分公司',
                           '10000元以上_03减免类_安徽分公司',
                           '10000元以上_03减免类_广东分公司',
                           '10000元以上_03减免类_宁夏分公司',
                           '10000元以上_03减免类_江西分公司',
                           '10000元以上_03减免类_青岛分公司',
                           '10000元以上_03减免类_上海分公司',
                           '10000元以上_03减免类_深圳分公司',
                           '10000元以上_03减免类_甘肃分公司',
                           '10000元以上_03减免类_海南分公司',
                           '10000元以上_03减免类_北京分公司',
                           '10000元以上_03减免类_云南分公司',
                           '10000元以上_03减免类_山东分公司',
                           '10000元以上_03减免类_重庆分公司',
                           '10000元以上_03减免类_广西分公司',
                           '10000元以上_03减免类_贵州分公司',
                           '10000元以上_03减免类_厦门分公司',
                           '10000元以上_03减免类_新疆分公司',
                           '10000元以上_03减免类_湖北分公司',
                           '10000元以上_03减免类_湖南分公司',
                           '10000元以上_03减免类_内蒙分公司',
                           '10000元以上_03减免类_天津分公司',
                           '10000元以上_03减免类_山西分公司',
                           '10000元以上_03减免类_西藏分公司',
                           '10000元以上_03减免类_江苏分公司',
                           '10000元以上_03减免类_陕西分公司',
                           '10000元以上_03减免类_河南分公司',
                           '10000元以上_04特殊类_黑龙江分公司',
                           '10000元以上_04特殊类_辽宁分公司',
                           '10000元以上_04特殊类_青海分公司',
                           '10000元以上_04特殊类_四川分公司',
                           '10000元以上_04特殊类_大连分公司',
                           '10000元以上_04特殊类_浙江分公司',
                           '10000元以上_04特殊类_吉林分公司',
                           '10000元以上_04特殊类_福建分公司',
                           '10000元以上_04特殊类_河北分公司',
                           '10000元以上_04特殊类_宁波分公司',
                           '10000元以上_04特殊类_安徽分公司',
                           '10000元以上_04特殊类_广东分公司',
                           '10000元以上_04特殊类_宁夏分公司',
                           '10000元以上_04特殊类_江西分公司',
                           '10000元以上_04特殊类_青岛分公司',
                           '10000元以上_04特殊类_上海分公司',
                           '10000元以上_04特殊类_深圳分公司',
                           '10000元以上_04特殊类_甘肃分公司',
                           '10000元以上_04特殊类_海南分公司',
                           '10000元以上_04特殊类_北京分公司',
                           '10000元以上_04特殊类_云南分公司',
                           '10000元以上_04特殊类_山东分公司',
                           '10000元以上_04特殊类_重庆分公司',
                           '10000元以上_04特殊类_广西分公司',
                           '10000元以上_04特殊类_贵州分公司',
                           '10000元以上_04特殊类_厦门分公司',
                           '10000元以上_04特殊类_新疆分公司',
                           '10000元以上_04特殊类_湖北分公司',
                           '10000元以上_04特殊类_湖南分公司',
                           '10000元以上_04特殊类_内蒙分公司',
                           '10000元以上_04特殊类_天津分公司',
                           '10000元以上_04特殊类_山西分公司',
                           '10000元以上_04特殊类_西藏分公司',
                           '10000元以上_04特殊类_江苏分公司',
                           '10000元以上_04特殊类_陕西分公司',
                           '10000元以上_04特殊类_河南分公司'],
        "credit_amount_columns": ['信用卡',
                                  '信用卡_上海分公司',
                                  '信用卡_云南分公司',
                                  '信用卡_内蒙分公司',
                                  '信用卡_北京分公司',
                                  '信用卡_厦门分公司',
                                  '信用卡_吉林分公司',
                                  '信用卡_四川分公司',
                                  '信用卡_大连分公司',
                                  '信用卡_天津分公司',
                                  '信用卡_宁夏分公司',
                                  '信用卡_宁波分公司',
                                  '信用卡_安徽分公司',
                                  '信用卡_山东分公司',
                                  '信用卡_山西分公司',
                                  '信用卡_广东分公司',
                                  '信用卡_广西分公司',
                                  '信用卡_新疆分公司',
                                  '信用卡_江苏分公司',
                                  '信用卡_江西分公司',
                                  '信用卡_河北分公司',
                                  '信用卡_河南分公司',
                                  '信用卡_浙江分公司',
                                  '信用卡_海南分公司',
                                  '信用卡_深圳分公司',
                                  '信用卡_湖北分公司',
                                  '信用卡_湖南分公司',
                                  '信用卡_甘肃分公司',
                                  '信用卡_福建分公司',
                                  '信用卡_西藏分公司',
                                  '信用卡_贵州分公司',
                                  '信用卡_辽宁分公司',
                                  '信用卡_重庆分公司',
                                  '信用卡_陕西分公司',
                                  '信用卡_青岛分公司',
                                  '信用卡_青海分公司',
                                  '信用卡_黑龙江分公司']
    }
}
