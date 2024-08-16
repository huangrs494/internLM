## api服务启动

1. 启动命令：lmdeploy serve api_server这个命令用于启动API服务器
2. 参数说明：
命令解释：
    --model-format hf：这个参数指定了模型的格式。hf代表“Hugging Face”格式。
    --quant-policy 0：这个参数指定了量化策略。qant_policy=4 表示 kv int4 量化，quant_policy=8 表示 kv int8 量化。
    --server-name 0.0.0.0：这个参数指定了服务器的名称。在这里，0.0.0.0是一个特殊的IP地址，它表示所有网络 接口。
    --server-port 23333：这个参数指定了服务器的端口号。在这里，23333是服务器将监听的端口号。
    --tp 1：这个参数表示并行数量（GPU数量）


